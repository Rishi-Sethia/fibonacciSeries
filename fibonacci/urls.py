'''
Created on 13-Apr-2019

@author: sethia
'''
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'getFibonacci$', views.getfibo, name='getfibo'),
#     url(r'getFibonacci/checkValue/(<nthvalue>\d+)?$', views.getNth, name='getNth'),
    url(r'getFibonacci/checkValue/(.*)$', views.getNth, name='getNth'),
]