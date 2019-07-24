#coding=utf-8

#当前用户信息
def getUserInfo(request):
    return {'suser':request.session.get('user',None)}