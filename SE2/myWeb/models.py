from django.db import models

# Create your models here.
"""
账户密码
"""
class Person(models.Model):
    name = models.CharField(primary_key=True,max_length=32)
    password = models.CharField(max_length=32)
    type = models.CharField(max_length=32)   #市民，政府或工人

"""
市民信息表
"""
class Citizen(models.Model):
    name = models.CharField(primary_key=True,max_length=10)
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)


"""
路面坑洼表
"""
class Hole(models.Model):
    citizen_name = models.CharField(max_length=32,default=" ")
    hole_id = models.CharField(primary_key=True,max_length=32)
    hole_street = models.CharField(max_length=32)
    hole_distinct = models.CharField(max_length=32,default="Baiyun")
    hole_location = models.CharField(max_length=32)
    hole_size = models.IntegerField(default=0)
    #数字从1开始，数字越小，优先级越高
    hole_priority = models.IntegerField(default=1)
    hole_status = models.CharField(default="waiting_for_repair",max_length=32)



