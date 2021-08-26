def newS(request):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "http://www.sdyu.edu.cn/index.htm",
    }
    url = 'http://www.sdyu.edu.cn/xwzx/tzgg.htm'
    if request.method == 'GET':
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
        # for ii in range(0,len(rhref)):
        #     rdesc=''
        #     html2 = requests.get(url=rhref[ii], headers=headers).text.encode('latin-1').decode('utf-8')
        #     html_tree2 = etree.HTML(html2)
        #     desc = html_tree2.xpath(
        #         "/html/body/div[3]/div/form/div/div/div/p/text()")
        #     for c in desc:
        #         rdesc += c + '\n'
        #     rrdesc.append(rdesc)
        # # if len(rtitle[0]) != 0:
        # nl = NewsLine()
        # for a in range(0,len(rtitle)):
        #     nl.title = rtitle[a]
        #     nl.href  = rhref[a]
        #     nl.subtitle = time[a]
        #     nl.body = rrdesc[a][0:160]
        #     nl.save()
        rdesc = ''
        html2 = requests.get(url=rhref[0], headers=headers).text.encode('latin-1').decode('utf-8')
        html_tree2 = etree.HTML(html2)
        desc = html_tree2.xpath(
            "/html/body/div[3]/div/form/div/div/div/p/text()")
        for c in desc:
            rdesc += c + '\n'
        rrdesc.append(rdesc)
        if len(rtitle[0]) != 0:
            nl = NewsLine()
            nl.title = rtitle[0]
            nl.href  = rhref[0]
            nl.subtitle = time[0]
            nl.body = rdesc[0:160]
            nl.save()
            return HttpResponse(
                rtitle[0]
            )
        else:
            return HttpResponse(
                'Faild'
            )