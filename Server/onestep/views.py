from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from onestep.models import Service, tabpanel, card


# Create your views here.

def get_index_page(request):
    return render(request, template_name='index.html')


def submit(request):
    if request.method == 'GET':
        return render(request, template_name='index.html')
    elif request.method == 'POST':
        sc = Service()
        sc.color = request.POST.get('inColor')
        sc.label = request.POST.get('inLabel')
        sc.icon = request.POST.get('inIcon')
        sc.href = request.POST.get('inHref')
        sc.type = request.POST.get('inType')
        sc.save()
    return HttpResponse('ok!')

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
        loc = request.GET.get('loc')
