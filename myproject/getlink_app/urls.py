from django import urls
from django.urls import path
from django.urls.conf import re_path
from .views import PageListView, PageDetailView
from .models import Page

app_name = 'getlink'

# Вариант 1.   '<slug>/'
# Вариант 2.   '<str:slug>/'
# Вариант 3.   '<slug:slug>/'

# from my_site.views import ArticleListView


urlpatterns = [
    path("slug/", PageListView.as_view(), name="list_slug"),
    path('<str:slug>/', PageDetailView.as_view(), name="details")
    # path('<slug:slug>/', PageDetailView.as_view(), name='detail_slug')

]