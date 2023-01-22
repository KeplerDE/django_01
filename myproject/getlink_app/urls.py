from django import urls
from django.urls import path
from django.urls.conf import re_path
from .views import PageListView, PageDetailView
from .models import Page

app_name = 'getlink'


# from my_site.views import ArticleListView


urlpatterns = [
    path("slug/", PageListView.as_view(), name="list_slug"),
    path('<slug>/', PageDetailView.as_view(), name="details")
    # path('<slug:slug>/', PageDetailView.as_view(), name='detail_slug')

]