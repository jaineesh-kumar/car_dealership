from .base import *

# Override production specific settings here
DEBUG = False
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
