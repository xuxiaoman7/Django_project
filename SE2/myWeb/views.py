from myWeb.models import Citizen
from myWeb.models import Hole


# Create your views here.

from distutils.command import register

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from myWeb.models import Person
from django.contrib import messages

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
        #储存citizen信息
        name = request.POST.get("name")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        citizen1 = Citizen(name = name,address = address,phone = phone)
        citizen1.save()
        #储存hole信息
        hole_street = request.POST.get("hole_street")
        hole_location = request.POST.get("hole_location")
        hole_size = request.POST.get("hole_size")
        hole_size_n = int(hole_size)
        #获取当前hole表的数据，为hole分配id
        hole_count = Hole.objects.all().count()
        hole_id = str(hole_count+1)
        #根据street确定distinct
        hole_distinct = ""
        if(hole_street=="内环东路"):
            hole_distinct = "番禺区"
        elif(hole_street=="北京路"):
            hole_distinct = "越秀区"
        else:
            hole_distinct = "Unclear"
        #根据size确定priority
        #历遍整个表找出有多少个size大于等于它的，假设有n个，那么priority就是n+1
        size_count = Hole.objects.filter(hole_size__gte=hole_size_n).count()
        hole_priority = size_count + 1
        #自动填充当前hole的hole status
        hole_status = "waiting_for_repair"
        #开始存入表中数据
        hole1 = Hole(citizen_name = name,hole_id = hole_id,hole_street = hole_street,hole_distinct= hole_distinct,hole_location = hole_location,hole_size = int(hole_size),hole_priority = hole_priority)
        hole1.save()
        #弹窗设置
        messages.success(request,'Save Successfully!')
        return render(request, 'citizen.html')


def Government(request):
    if request.method == "GET":
        #这里要获取表里hole的个数
        number_of_hole = 9
        hole_number = "Hole_ID:00" + str(number_of_hole)
        return render(request,'Government.html',{"hole_number":hole_number})
    if request.method == "POST":
        pass

def Worker(request):
    if request.method == "GET":
        #这里需要获取hole里优先级最高的信息
        hole_id = "Hole_ID:001"
        required_material = "Reqired_Material:material1"
        required_equpiment = "Required_Equipment:equipment1"
        return render(request,"Worker.html",{"hole_id":hole_id,"required_material":required_material,"required_equipment":required_equpiment})
    if request.method == "POST":
        pass


