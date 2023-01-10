from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),         # переменная list  пространство имен


]