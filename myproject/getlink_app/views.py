from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Page

# Извлечение url по slug
class PageListView(ListView):
    model = Page
    template_name = "slug_url/list_slug.html"

class PageDetailView(DetailView):
    model = Page
    context_object_name = 'detail_slug'
    template_name = "slug_url/detail_slug.html"