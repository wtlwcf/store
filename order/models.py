#coding=utf-8
from django.db import models
from user.models import Address, UserInfo


#订单
class Order(models.Model):
    #uuid全球唯一字符串编码，订单编号，以表id自动填充
    out_trade_num=models.UUIDField()
    order_num=models.CharField(max_length=50)
    # 扫码支付自动生成编号字段
    trade_no=models.CharField(max_length=120)
    #状态，支付，待支付
    status=models.CharField(max_length=20)
    #支付方式
    payway=models.CharField(max_length=20,default='alipay')
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    user=models.ForeignKey(UserInfo,on_delete=models.CASCADE)

 #订单选项
class OrderItem(models.Model):
    goodsid=models.PositiveIntegerField()
    sizeid = models.PositiveIntegerField()
    colorid = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    order=models.ForeignKey(Order,on_delete=models.CASCADE)









