# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from user.models import *
from utils.code import *
from django.core.serializers import serialize  # 序列化
from cart.cartmanager import *


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        # 获取请求参数
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        # 插入数据库
        user = UserInfo.objects.create(uname=uname, pwd=pwd)

        # 判断是否注册成功
        if user:
            # 将用户信息存放至session对象中
            request.session['user'] = user

            return HttpResponseRedirect('/user/center/')

        return HttpResponseRedirect('/user/register/')


class CheckUnameView(View):
    def get(self, request):
        # 获取请求参数
        uname = request.GET.get('uname')

        # 根据用户名去数据库中查询
        userList = UserInfo.objects.filter(uname=uname)

        flag = False

        # 判断是否存在
        if userList:
            flag = True

        return JsonResponse({'flag': flag})


class CenterView(View):
    def get(self, request):
        return render(request, 'center.html')


class Logoutview(View):
    def post(self, request):
        # 删除session中所有数据
        if 'user' in request.session:
            del request.session['user']
        return JsonResponse({'delflag': True})


class Loginview(View):
    def get(self, request):
        # 判断用户是否登录状态
        # 获取请求参数
        red = request.GET.get('redirect')

        return render(request, 'login.html', {'redirect': red})

    def post(self, request):
        # 获取请求参数
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        # 查询数据库中是否存在
        userlist = UserInfo.objects.filter(uname=uname, pwd=pwd)
        if userlist:
            request.session['user'] = userlist[0]
            red = request.POST.get('redirect')
            if red == 'cart':
                # 将session中的购物项移动到数据库
                SessionCartManager(request.session).migrateSession2DB()
                return HttpResponseRedirect('/cart/queryAll')
            elif red == 'order':
                return HttpResponseRedirect('/order/order.html?cartitems='+request.POST.get('cartitems'))

            return HttpResponseRedirect('/user/center/')
        return HttpResponseRedirect('/user/login/')


class LoadCodeView(View):
    def get(self, request):
        img, str = gene_code()
        # 将生成的验证码存放到session中
        request.session['sessionCode'] = str
        # print(str)

        return HttpResponse(img, content_type='image/png')


class CheckCodeView(View):
    def get(self, request):
        # 获取输入框的验证码
        code = request.GET.get('code')
        # 获取生成的验证码
        sessioncode = request.session.get('sessionCode', None)
        # 比较是否相等
        flag = code == sessioncode
        # print(flag)
        return JsonResponse({'checkFlag': flag})


class AddressView(View):
    def get(self, request):
        user = request.session.get('user', '')

        # 获取当前登录用户的所有收货地址
        addrList = user.address_set.all()

        return render(request, 'address.html', {'addrList': addrList})

    def post(self, request):
        # 获取请求参数
        aname = request.POST.get('aname', '')
        aphone = request.POST.get('aphone', '')
        addr = request.POST.get('addr', '')
        user = request.session.get('user', '')

        # 将数据插入数据库
        address = Address.objects.create(aname=aname, aphone=aphone, addr=addr, userinfo=user,
                                         isdefault=(lambda count: True if count == 0 else False)(
                                             user.address_set.all().count()))

        # 获取当前登录用户的所有收货地址
        addrList = user.address_set.all()

        return render(request, 'address.html', {'addrList': addrList})


class LoadAreaView(View):
    def get(self, request):
        # 获取请求参数
        pid = request.GET.get('pid', -1)
        pid = int(pid)

        # 根据父id查询区划信息
        areaList = Area.objects.filter(parentid=pid)

        # 进行序列化
        jareaList = serialize('json', areaList)

        return JsonResponse({'jareaList': jareaList})
