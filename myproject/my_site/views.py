from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Articles

from typing import Reversible
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Absolute

# my_site/templates/my_site/articles_list.html

class ArticleListView(ListView):
    model = Articles
    

class ArtickeDetailView(DetailView): 
    model = Articles
    context_object_name = 'art'



#namespace


# Извлечение url по slug
class AbsoluteListView(ListView):
    model = Absolute
    template_name = "my_site/get_absolute/list_get_absolute.html"
    #context_object_name = 'pg'
    
    
   
class AbsoluteDetailView(DetailView):
    model = Absolute
    template_name = "my_site/get_absolute/detail_get_absolute.html" 
    context_object_name = 'mmm'

    

    

   


