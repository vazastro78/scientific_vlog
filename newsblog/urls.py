from django.urls import path

from mainapp.apps import MainappConfig
from newsblog.views import ArticleListView, ArticleCreateView, ArticleDetailView

app_name = MainappConfig.name

urlpatterns = [
#    path('', index, name='index'),
    path('', ArticleListView.as_view(), name='listallarticles'),
    path('create/', ArticleCreateView.as_view(), name='create_single_article'),
    path('view/<int:pk>/', ArticleDetailView.as_view(), name='view_single_article'),
]
