import json

from django.http import HttpResponse, JsonResponse
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
    def get(self, request, phone_num):
        name = request.GET.get('name')
        return HttpResponse(f'{name}注册页面{phone_num}')

    def post(self, request):
        query_dict = request.POST
        print(query_dict.get('age'))
        json_str = request.body
        json_dict = json.loads(json_str)
        print(json_dict)
        return HttpResponse('注册逻辑')

    def put(self, request, phone_num):
        dict_1 = {'name': '小明', 'age': 18}
        return JsonResponse(dict_1)
