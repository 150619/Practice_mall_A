import json

from django.http import JsonResponse
from django.views import View

from apps.users.models import User


class RegisterName(View):
    # 解析路径参数
    def get(self, request, username):
        # 与数据库中数据做对比
        count = User.objects.filter(username=username).count()
        if count > 0:
            return JsonResponse({'code': '400', 'errmsg': '用户名已存在', 'count': count})
        else:
            return JsonResponse({'code': '0', 'errmsg': 'ok', 'count': count})


class RegisterMobile(View):
    def get(self, request, mobile):
        count = User.objects.filter(mobile=mobile).count()
        if count > 0:
            return JsonResponse({'code': '400', 'errmsg': '手机号已存在', 'count': count})
        else:
            return JsonResponse({'code': '0', 'errmsg': 'ok', 'count': count})


class Register(View):
    def post(self, request):
        # 解析请求体参数
        json_dict = json.loads(request.body)
        # 获取username
        username = json_dict.get('username')
        # 判断数据库中是否已经存在一个username
        count = User.objects.filter(username=username).count()
        # 存在返回错误码
        if count > 0:
            return JsonResponse({'code': '400', 'errmsg': '用户名已存在'})
        # 获取password和password2
        password = json_dict.get('password')
        password2 = json_dict.get('password2')
        # 判断password和password2是否相等,不相等返回错误码
        if password != password2:
            return JsonResponse({'code': '400', 'errmsg': '两次输入的密码不一致'})
        # 获取mobile
        mobile = json_dict.get('mobile')
        # 判断手机号是否存在
        count = User.objects.filter(mobile=mobile).count()
        if count > 0:
            return JsonResponse({'code': '400', 'errmsg': '手机号已存在'})
        # 判断手机号格式

        # 获取sms_code
        # sms_code = json_dict.get('sms_code')
        # 与redis中的真实验证码做对比
        # 如果不相等返回错误码

        # 获取allow
        allow = json_dict.get('allow')
        # 不是True返回错误码
        if allow != 'True':
            return JsonResponse({'code': '400', 'errmsg': '请同意用户协议'})
        # 将获取到的数据保存到数据库
        User.objects.create(username=username, password=password, mobile=mobile)
        return JsonResponse({'code': '0', 'errmsg': 'ok'})
