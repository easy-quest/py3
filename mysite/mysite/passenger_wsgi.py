import os, sys
site_user_root_dir = '/home/e/easyqubx/easyqubx.beget.tech/public_html'
sys.path.insert(0, site_user_root_dir + '/mysite')
sys.path.insert(1, site_user_root_dir + '/venv/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
