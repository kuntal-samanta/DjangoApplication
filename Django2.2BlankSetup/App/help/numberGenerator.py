'''
    Help Package
   @ Author  Kuntal
   @ Company 
   @ version  0.1
   @date      10/12/2019
'''

import secrets
import string
import os
import sys


def Number_Generator_4():
    letters = string.ascii_letters + string.digits + string.hexdigits
    l = [secrets.choice(letters) for i in range(4)]
    num = ''
    for i in l:
        num = num + i
    return num


def Number_Generator_6():
    letters = string.ascii_letters + string.digits + string.hexdigits
    l = [secrets.choice(letters) for i in range(6)]
    num = ''
    for i in l:
        num = num + i
    return num


def Number_Generator_8():
    letters = string.ascii_letters + string.digits + string.hexdigits
    l = [secrets.choice(letters) for i in range(8)]
    num = ''
    for i in l:
        num = num + i
    return num


def Number_Generator_16():
    letters = string.ascii_letters + string.digits + string.hexdigits
    l = [secrets.choice(letters) for i in range(16)]
    num = ''
    for i in l:
        num = num + i
    return num
