import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class BookView(View):
    def post(self, request):
        json_dict = json.loads(request.body)
        name = json_dict.get('name')
        age = json_dict.get('age')
        print(name)
        print(type(name))
        print(age)
        print(type(age))
        # return HttpResponse('Successful')
        request.session['name'] = str(name)
        request.session['age'] = str(age)
        response = HttpResponse(name)
        response.set_cookie(key='name', value='LiSi', max_age=3600)
        return response

    def get(self, request):
        name = request.session.get('name')
        print(name)
        return HttpResponse(f'{name}')
