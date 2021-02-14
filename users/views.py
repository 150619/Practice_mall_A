from django.http import HttpResponse
from django.shortcuts import render

# def register(request):
#     if request.method == 'GET':
#         return HttpResponse('注册页面')
#     if request.method == 'POST':
#         return HttpResponse('提交注册信息')
from django.utils.decorators import method_decorator
from django.views import View


def my_decorator(func):
    def inner_func(request, *args, **kwargs):
        print(f'请求路径{request.path}')
        result = func(request, *args, **kwargs)
        return result

    return inner_func


@method_decorator(my_decorator, name='post')
class Register(View):
    @method_decorator(my_decorator)
    def get(self, request):
        return HttpResponse('注册页面')

    def post(self, request):
        return HttpResponse('注册逻辑')
