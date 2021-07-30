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


# def sJxfwApi(request):
#     if request.method == 'GET':
#         type = request.GET.get('type')
#         a = Service.objects.values().filter(type=type)
#         r = HttpResponse('aaaa')
#         if type == '0':
#             b = []
#             c = []
#             for i in range(0, 4):
#                 b.append(a[i])
#                 c.append(a[i + 4])
#             # return HttpResponse(a)
#             r = JsonResponse(
#                 {
#                     "list": {
#                         "page1": b,
#                         "page2": c,
#                     }
#                 }
#             )
#         elif type == '1':
#             b = []
#             for i in range(0, len(a)):
#                 b.append(a[i])
#             r = JsonResponse(
#                 {
#                     "data": b
#                 }
#             )
#         elif type == '2':
#             b = []
#             for i in range(0, len(a)):
#                 b.append(a[i])
#             r = JsonResponse(
#                 {
#                     "data": b
#                 }
#             )
#         elif type == '3':
#             b = []
#             for i in range(0, len(a)):
#                 b.append(a[i])
#             r = JsonResponse(
#                 {
#                     "data": b
#                 }
#             )
#         elif type == '4':
#             b = []
#             for i in range(0, len(a)):
#                 b.append(a[i])
#             r = JsonResponse(
#                 {
#                     "data": b
#                 }
#             )
#
#         return r

def sJxfwApi(request):
    if request.method == 'GET':
        a = Service.objects.values().all()
        r ={"jxfwList":{},"shfwList":{},"chwlList":{}}
        jxfwList ={"page1":[],"page2":[]}
        shfwList = {"data":[]}
        chwlList = {'ct':[],'yp':[],'gc':[]}
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
                chwlList['ct'].append(a[i])
                r["chwlList"]['ct'] = chwlList['ct']
            elif a[i]["type"] == 3:
                chwlList['yp'].append(a[i])
                r["chwlList"]['yp'] = chwlList['yp']
            elif a[i]["type"] == 4:
                chwlList['gc'].append(a[i])
                r["chwlList"]['gc'] = chwlList['gc']
    return JsonResponse(r)
