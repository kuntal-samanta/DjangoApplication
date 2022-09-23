from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')

    def handle(self, *args, **kwargs):
        print("---------->kwargs : ", kwargs)
        '''
            > python manage.py create_users 5 --admin
            
            kwargs :  {
                'verbosity': 1, 'settings': None, 'pythonpath': None, 
                'traceback': False, 'no_color': False, 'force_color': False, 
                'skip_checks': False, 'total': 5, 'admin': True}
        '''
        total = kwargs['total']
        print("total : ", total, type(total))
        if kwargs['admin']:
            is_superuser = True
            is_staff=True
        else:
            is_superuser = False
            is_staff=False
        
        for i in range(total):
            v = random.randint(100, 100) * random.randint(100, 10000)
            v = str(v)
            User.objects.create_user(
                first_name=v,
                last_name=v,
                username=v, 
                email=v + "@mail.com", 
                password='12345',
                is_superuser=is_superuser,
                is_staff=is_staff
            )

"""
    How to use

> python manage.py create_users 5

> python manage.py create_users 5 -a 
    OR 
>python manage.py create_users 5 --admin
"""

