from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog, Articles


class ArticleListView(ListView):
    model = Articles
    template_name = 'articles_list.html'


class ArticleDetailView(DetailView):
    model = Articles
    context_object_name = 'art'
    template_name = 'article_detail.html'
