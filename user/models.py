# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    areaid = models.IntegerField(primary_key=True)
    areaname = models.CharField(max_length=50)
    parentid = models.IntegerField()
    arealevel = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'area'


class UserInfo(models.Model):
    uname = models.EmailField(max_length=100)  # 用户是邮箱注册
    pwd = models.CharField(max_length=100)

    def __str__(self):
        return 'UserInfo:%s' % self.uname


class Address(models.Model):
    aname = models.CharField(max_length=30)  # 收件人
    aphone = models.CharField(max_length=11)
    addr = models.CharField(max_length=100)  # 地址
    isdefault = models.BooleanField(default=False)  # 是否默认地址
    userinfo = models.ForeignKey('UserInfo', models.CASCADE)  # 外键，对应userinfo

    def __str__(self):
        return 'Address:%s' % self.aname
