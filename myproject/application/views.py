from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog


class ArticleListView(ListView):
    model = Blog
    template_name = 'index.html'
