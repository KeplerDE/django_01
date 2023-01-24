from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Page

# Извлечение url по slug
class PageListView(ListView):
    model = Page
    template_name = "slug_url/list_slug.html"

class PageDetailView(DetailView):
    model = Page
    context_object_name = 'details'          # обращаемся в шаблоне по такому фрагменту
    template_name = "slug_url/detail_slug.html"


class PageListNamespace(ListView):
    model = Page
    template_name = "namespace/list_ns.html"
    context_object_name = 'pg'


class PageDetailNamespace(DetailView):
    model = Page
    template_name = "namespace/detail_ns.html"
    context_object_name = 'details'          # обращение по контексту
    # https://tutorial.djangogirls.org/en/extend_your_application/
    #https://docs.djangoproject.com/en/4.1/ref/class-based-views/mixins-single-object/

# переопределение get_absolute_url

class PageListGetAbsoluteUrl(ListView):
    model = Page
    template_name = "get_absolute_url/list_get_absolute_url.html"
    context_object_name = 'pg'


class PageDetailGetAbsoluteUrl(DetailView):
    model = Page
    template_name = "get_absolute_url/detail_get_absolute_url.html"
    context_object_name = 'details'


