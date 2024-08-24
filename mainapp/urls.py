from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import index
from newsblog.views import ArticleListView

app_name = MainappConfig.name

urlpatterns = [
    path('', ArticleListView.as_view(), name='listallarticles')
]
