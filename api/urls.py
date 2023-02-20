from django.urls import path, include
from rest_framework import routers
import importlib
import inspect

router = routers.DefaultRouter()

module_name = 'api.views'
views_module = importlib.import_module(module_name)
for name, obj in inspect.getmembers(views_module):
    if inspect.isclass(obj) and name.endswith('ViewSet'):
        router.register(r'%s' % name[:-7].lower(), obj)

urlpatterns = [
    path('', include(router.urls))
]
