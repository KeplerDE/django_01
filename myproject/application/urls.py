from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import ArticleListView, ArticleDetailView

myapp = 'application'


urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),         # переменная list  пространство имен, для временной паеременной в итераторах
    path("<slug:slug>/", ArticleDetailView.as_view(), name='article-detail'),



]