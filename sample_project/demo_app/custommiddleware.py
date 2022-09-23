from datetime import datetime, timedelta
from django.core.cache import cache
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class KuntalDemoMiddleware(MiddlewareMixin):
    def process_request(self, request):
        cache.set('xxx', 11111)
        print("###############################")
        print('\n', '          My Middleware         ', '\n')
        print("###############################")
        # print(request.META)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print("Your Ip is : ", ip)

        ip_list = ['172.10.123.1', '172.10.123.2', '172.10.123.3', '127.0.0.1']

        if ip in ip_list:
            print("Your Are Welcome")
        else:
            print("!!!!!!!!!!!!!!!!!!!")



"""
# import custom middleware

'demo_app.custommiddleware.KuntalDemoMiddleware',
"""