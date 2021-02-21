from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection

from apps.verification.captcha.captcha import captcha


class ImageCodes(View):
    def get(self, request, uuid):
        # 生成图形验证码
        text, image = captcha.generate_captcha()
        # 保存图形验证码,连接redis数据库(别名),redis数据库添加(字符串类型)
        redis_connect = get_redis_connection('verify_code')
        redis_connect.setex(f'code_{uuid}', 300, text)
        # content_type是响应体数据类型
        return HttpResponse(image, content_type='image/jpg')
