import os
import sys
import site


paths = [ '/var/www/vhosts/vps42667.ovh.net/test.ewmitaly.net/sagitairbox/sagitair/',
          '/var/www/vhosts/vps42667.ovh.net/test.ewmitaly.net/sagitairbox',
          '/var/www/vhosts/vps42667.ovh.net/test.ewmitaly.net/sagitairbox/lib/python2.7/site-packages/',
]

for path in paths:
    if path not in sys.path:
        sys.path.append(path)


# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/var/www/vhosts/vps42667.ovh.net/test.ewmitaly.net/sagitairbox/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/vhosts/vps42667.ovh.net/test.ewmitaly.net/sagitairbox')
sys.path.append('/var/www/vhosts/vps42667.ovh.net/test.ewmitaly.net/sagitairbox/sagitair')

os.environ['DJANGO_SETTINGS_MODULE'] = 'sagitair.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/var/www/vhosts/vps42667.ovh.net/test.ewmitaly.net/sagitairbox/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()