from django.urls import path

from mainapp.apps import MainappConfig
from newsblog.views import index

app_name = MainappConfig.name

urlpatterns = [
    path('', index, name='index'),
]
