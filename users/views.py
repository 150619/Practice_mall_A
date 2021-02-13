from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    if request.method == 'GET':
        return HttpResponse('注册页面')
    if request.method == 'POST':
        return HttpResponse('提交注册信息')
