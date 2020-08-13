'''
    Help Package
   @ Author  Kuntal
   @ Company 
   @ version  0.1
   @date      10/12/2019
'''

import httpagentparser
import os, sys


def GetRemotePCIP(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
