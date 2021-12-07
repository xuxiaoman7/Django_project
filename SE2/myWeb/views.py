from myWeb.models import Citizen
from myWeb.models import Hole


# Create your views here.

from distutils.command import register

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from myWeb.models import Person

def index(request):
   return render(request,"index.html")

#def Login_form(request):
#    return render(request, 'login.html')

def Login(request):
    if request.method == "GET":
        return render(request,'login.html')
    if request.method == 'POST' and request.POST:
        type = request.POST.get("type")
        name = request.POST.get("name")
        password = request.POST.get("password")
        e = Person.objects.filter(name=name,type=type).first()
        if e:
            now_password = password
            db_password = e.password
            if now_password == db_password:
                #respone = render(request,'index.html')
                if type=='citizen':
                    respone = redirect('/Citizen/')
                if type == 'government':
                    respone = redirect('/Government/')
                if type == 'worker':
                    respone = redirect('/Worker')
                return respone
    return render(request,"login.html")

def Citizen(request):
    if request.method == "GET":
        return render(request,'citizen.html')
    if request.method == 'POST' and request.POST:
        name = request.POST.get("name")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        hole_street = request.POST.get("hole_street")
        hole_location = request.POST.get("hole_location")
        hole_size = request.POST.get("hole_size")
        #获取当前hole表的数据，为hole分配id
        hole_id = ""
        #根据street确定distinct
        hole_distinct = ""
        #根据size确定priority
        #历遍整个表找出有多少个size大于等于它的，假设有n个，那么priority就是n+1
        hole_priority = 2
        #自动填充当前hole的hole status
        hole_status = "waiting_for_repair"
        hole1 = Hole(hole_id = hole_id,hole_street = hole_street,hole_distinct= hole_distinct,hole_location = hole_location,hole_size = int(hole_size),hole_priority = hole_priority)
        hole1.save()
        return HttpResponse("<p>Add Successfully!</p>")


def Government(request):
    if request.method == "GET":
        #这里要获取表里hole的个数
        hole_number = 9
        return render(request,'Government.html',{"hole_number":hole_number})
    if request.method == "POST":
        pass

def Worker(request):
    if request.method == "GET":
        #这里需要获取hole里第一行的信息
        hole_id = "001"
        required_material = "material"
        required_equpiment = "equipment"
        return render(request,"Worker.html",{"hole_id":hole_id,"required_material":required_material,"required_equipment":required_equpiment})
    if request.method == "POST":
        pass


def runoob(request):
    #创建字典context
    #context = {}
    #键值为’hello‘的值为该字符串
    #context['hello'] = 'Hello world!'
    #传入该字典
    #return render(request,'index.html',context)

    #views_name = "教程"
    #return render(request,"index.html",{"name":views_name})

    #views_str = "<a href = 'https://www.runoob.com/'>点击跳转</a>"
    #return render(request,"index.html",{"views_str":views_str})
    return render(request,"index.html")