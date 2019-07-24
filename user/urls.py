# coding=utf-8

# coding=utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.RegisterView.as_view()),
    url(r'^checkUname/$', views.CheckUnameView.as_view()),
    url(r'^center/$', views.CenterView.as_view()),
    url(r'^logout/$', views.Logoutview.as_view()),
    url(r'^login/$', views.Loginview.as_view()),
    url(r'^loadCode.jpg/$', views.LoadCodeView.as_view()),
    url(r'^checkCode/$', views.CheckCodeView.as_view()),
    url(r'^address/$',views.AddressView.as_view()),
    url(r'^loadArea/$',views.LoadAreaView.as_view())
]
