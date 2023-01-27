from django import urls

from django.urls import path
from django.urls.conf import  re_path, path
from .views import ArticleListView, ArtickeDetailView
from .views import AbsoluteListView, AbsoluteDetailView

app_name = 'ab_ns2'

# https://fixmypc.ru/post/sozdanie-ssylok-metodom-get-absolute-v-python-django-3/

#app_name = 'yes_ns'
urlpatterns = [
    re_path(r'^$', ArticleListView.as_view(), name='list'),
    
    #path("<int:slug>/", ArtickeDetailView.as_view(), name='article-detail'),
    path("<slug:slug>/", ArtickeDetailView.as_view(), name='article-detail'),


    # namespace='yes_ns'
    path('list/all/', AbsoluteListView.as_view(), name='list_mns'),
    path('detail/<int:pk>/<str:slug>/', AbsoluteDetailView.as_view(), name="detail_mns"),
    
]


