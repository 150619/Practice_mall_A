from django.utils.deprecation import MiddlewareMixin


class TestMiddleware1(MiddlewareMixin):
    def process_request(self, request):
        print('请求前1')

    def process_response(self, request, response):
        print('响应返回给客户端之前1')
        return response


class TestMiddleware2(MiddlewareMixin):
    def process_request(self, request):
        print('请求前2')

    def process_response(self, request, response):
        print('响应返回给客户端之前2')
        return response
