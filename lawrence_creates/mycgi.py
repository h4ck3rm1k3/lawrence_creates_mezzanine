import sys, os
sys.path += ['/var/chroot/home/content/55/10855655/opt/vhost/chroot/sl5-v1/root']
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
from flup.server.fcgi import WSGIServer
from django.core.handlers.wsgi import WSGIHandler
WSGIServer(WSGIHandler()).run()
