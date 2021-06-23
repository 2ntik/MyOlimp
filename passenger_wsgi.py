# -*- coding: utf-8 -*-
import os
import sys
from django.core.wsgi import get_wsgi_application


sys.path.insert(0, '/var/www/u1396862/data/www/myolimp.online/MyOimp')
sys.path.insert(1, '/var/www/u1396862/data/djangovenv/lib/python3.7.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'MyOlimp.settings'
application = get_wsgi_application()
