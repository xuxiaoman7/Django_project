from django.http import HttpResponse
from django.shortcuts import render

#表单
def search_form(request):
    return render(request,'search_form.html')

#接收请求数据
def search(request):
    if 'q' in request.GET and request.GET['q']:
        message = 'What you search for is ' + request.GET['q']
    else:
        message = 'You submit the empty form'
    return HttpResponse(message)