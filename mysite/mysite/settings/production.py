from .base import *

DEBUG = False

ALLOWED_HOSTS = ['ppaiorg.in']

ROOT_URLCONF = 'mysite.urls'

SECRET_KEY = "^wz1=*mzco0k^5ta*&w7*ql^*-7pt3##c+$&a%xll)h7*7zizp"


try:
    from .local import *
except ImportError:
    pass
