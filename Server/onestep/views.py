from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from onestep.models import Service, tabpanel, card,banner,NewsLine
import requests,re
from lxml import etree

# Create your views here.

def get_index_page(request):
    return render(request, template_name='serviceSubmit.html')


def serviceSubmit(request):
    if request.method == 'GET':
        return render(request, template_name='serviceSubmit.html')
    elif request.method == 'POST':
        sc = Service()
        sc.color = request.POST.get('inColor')
        sc.label = request.POST.get('inLabel')
        sc.icon = request.POST.get('inIcon')
        sc.href = request.POST.get('inHref')
        sc.type = request.POST.get('inType')
        sc.save()
    return HttpResponse('ok!')

def tabpanelSubmit(request):
    if request.method == 'GET':
        return render(request,template_name='tabpanelSubmit.html')
    elif request.method == 'POST':
        tp = tabpanel()
        tp.label = request.POST.get('inLabel')
        tp.pos = request.POST.get('inpos')
        tp.loc = request.POST.get('inloc')
        tp.save()
    return HttpResponse('ok!')

def submitApi(request):
    if request.method == 'GET':
        return HttpResponse('Connect ok')

    elif request.method == 'POST':
        return HttpResponse(request.POST.get('label')+request.POST.get('pos'))

def sJxfwApi(request):
    if request.method == 'GET':
        a = Service.objects.values().all()
        r ={"jxfwList":{},"shfwList":{},"chwlList":{}}
        jxfwList ={"page1":[],"page2":[]}
        shfwList = {"data":[]}
        chwlList = {'ct':{'list':[],'label':'餐厅'},'yp':{'list':[],'label':'饮品'},'gc':{'list':[],'label':'北苑广场'}}
        for i in range(len(a)):
            if a[i]['type'] == 0:
                if i < 4:
                    jxfwList["page1"].append(a[i])
                else:
                    jxfwList["page2"].append(a[i])
                r["jxfwList"] = jxfwList
            elif a[i]['type'] == 1:
                shfwList['data'].append(a[i])
                r["shfwList"] = shfwList
            elif a[i]["type"] == 2:
                chwlList['ct']['list'].append(a[i])
                r["chwlList"]['ct'] = chwlList['ct']
            elif a[i]["type"] == 3:
                chwlList['yp']['list'].append(a[i])
                r["chwlList"]['yp'] = chwlList['yp']
            elif a[i]["type"] == 4:
                chwlList['gc']['list'].append(a[i])
                r["chwlList"]['gc'] = chwlList['gc']
    return JsonResponse(r)

def tabpanelApi(request):
    if request.method == 'GET':
        pos = request.GET.get('pos')
        # loc = request.GET.get('loc')
        a = tabpanel.objects.values().filter(pos=pos)
        tab = []
        for i in range(0,len(a)):
            tab.append(a[i])
        r={"tab":tab}
        return JsonResponse(r)

def cardApi(request):
    if request.method == 'GET':
        c = card.objects.values('cName_id').distinct()
        a = card.objects.values().all()
        tabList = []
        cardList=[]
        for i in range(0,len(c)):
            tabList.append(c[i]['cName_id'])
        for ii in range(0,len(a)):
            cardList.append(a[ii])
        r = {}
        # 将不同位置的商铺分组
        for iii in cardList:
            for iiii in tabList:
                if iii['cName_id'] == iiii: #判断商铺名称是否与数据库中遍历出的商铺名称相同
                    cardListlist = []
                    cardListlist.append(iii)
                r[iiii]=cardListlist
        return  JsonResponse(r)

def bannerApi(request):
    if request.method == 'GET':
        a =banner.objects.values()
        img = []
        for i in range(0,len(a)):
            img.append(a[i])
        r={"banner":img}
        return JsonResponse(r)

def NewsApi(request):
    if request.method == 'GET':
        a=NewsLine.objects.values().order_by('-subtitle')[:3]
        news = []
        for i in range(0, len(a)):
            news.append(a[i])
        r = {"news": news}
        return JsonResponse(r)

def newS(request):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "http://www.sdyu.edu.cn/index.htm",
    }
    url = 'http://www.sdyu.edu.cn/xwzx/tzgg.htm'
    html = requests.get(url=url, headers=headers).text.encode('latin-1').decode('utf-8')
    html_tree = etree.HTML(html)
    title = html_tree.xpath(
        "/html/body/div[@class='wp-wrapper']/div[@class='wp-inner']/ul[@class='subnews-list']/a/li/text()")
    # title = html_tree.xpath(
    #     "/html/body/div[@class='wp-wrapper']/div[@class='wp-inner']/ul[@class='subnews-list']/a[@id='line_u6_0']/li/text()")
    time = html_tree.xpath(
        "/html/body/div[@class='wp-wrapper']/div[@class='wp-inner']/ul[@class='subnews-list']/a/li/span/text()")
    href = html_tree.xpath(
        "/html/body/div[@class='wp-wrapper']/div[@class='wp-inner']/ul[@class='subnews-list']/a/@href")
    rtitle = []
    rhref = []
    rrdesc = []
    for i in title:
        i = re.sub("\r\n", '', i)
        i = re.sub(" ", '', i)
        if len(i) != 0:
            rtitle.append(i)
    for i in href:
        i = re.sub("^..", '', i)
        i = 'http://www.sdyu.edu.cn' + i
        rhref.append(i)
    for ii in range(0,len(rhref)):
        rdesc=''
        html2 = requests.get(url=rhref[ii], headers=headers).text.encode('latin-1').decode('utf-8')
        html_tree2 = etree.HTML(html2)
        desc = html_tree2.xpath(
            "/html/body/div[3]/div/form/div/div/div/p/text()")
        for c in desc:
            rdesc += c + '\n'
        rrdesc.append(rdesc)
    nl = NewsLine()
    if len(rtitle[0]) != 0:
        for a in range(0,len(rtitle)):
            nl.title = rtitle[a]
            nl.href  = rhref[a]
            nl.subtitle = time[a]
            nl.body = rrdesc[a][0:140]
            nl.save()
        return HttpResponse(
            rtitle
        )
    else:
        return HttpResponse(
            'Faild'
        )
#https://blog.csdn.net/u014368609/article/details/72524476