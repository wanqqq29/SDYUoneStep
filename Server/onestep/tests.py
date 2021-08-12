from django.test import TestCase
import requests,re
from lxml import etree
# Create your tests here.
def newS():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "http://www.sdyu.edu.cn/index.htm",
    }
    url='http://www.sdyu.edu.cn/xwzx/tzgg.htm'
    html = requests.get(url=url,headers=headers).text.encode('latin-1').decode('utf-8')
    html_tree = etree.HTML(html)
    title = html_tree.xpath("/html/body/div[@class='wp-wrapper']/div[@class='wp-inner']/ul[@class='subnews-list']/a[@id='line_u6_0']/li/text()")
    time = html_tree.xpath("/html/body/div[@class='wp-wrapper']/div[@class='wp-inner']/ul[@class='subnews-list']/a[@id='line_u6_0']/li/span/text()")
    href = html_tree.xpath("/html/body/div[@class='wp-wrapper']/div[@class='wp-inner']/ul[@class='subnews-list']/a[@id='line_u6_0']/@href")
    rtitle = []
    rhref = []
    for i in title:
        i = re.sub("\r\n",'',i)
        i = re.sub(" ",'',i)
        if len(i) != 0:
            rtitle.append(i)
    for i in href:
        i = re.sub("^..",'',i)
        i = 'http://www.sdyu.edu.cn'+i
        rhref.append(i)
    print(rhref)
    print(rtitle,type(rtitle))
    print(time,type(time))
