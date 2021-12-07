"""SE2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myWeb import views
from django.conf.urls import url
from . import search


#绑定跳转的路径与方法
urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^Login',views.Login),
    #登录界面
    #url('Login_form/',views.Login_form),

    #登录界面
    url('Login/',views.Login),
    #url('runoob/',views.runoob),
    #url(r'^search-form/$',search.search_form),
    #url(r'^search/$',search.search),
    url('index/',views.index),
    url('Citizen/',views.Citizen),
    url('Government/',views.Government),
    url('Worker/',views.Worker),
]
