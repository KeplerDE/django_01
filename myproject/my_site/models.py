# -*- coding: utf-8 -*-

from typing import Reversible
from django.db import models
from django.shortcuts import reverse

class Absolute(models.Model):
    class Meta:
        verbose_name = "Absolute list"
        verbose_name_plural = "Absolute Lists"


    name = models.CharField(max_length=160)
    content = models.TextField(blank=True)
    #img = models.ImageField()
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    """
    def get_absolute_url(self):
        return f'/article/{self.pk}/'
    """   
        #return reverse('people.views.details', args=[str(self.id)])
        
        #return reverse('ab_ns:detail_mns',kwargs={'pk': self.pk})

    
    def get_absolute_url(self):
            #reverse('list_mns', current_app=self.request.resolver_match.namespace)
            return reverse('ab_ns2:detail_mns', 
                           
                           #args=[str(self.pk, self.slug)])  
                           kwargs={'pk': self.pk, "slug": self.slug})      
    


class Articles(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    #template_name = ""
 
    def __str__(self):
        return self.title

   





"""
alias ma='python manage.py makemigrations'
alias mi='python manage.py migrate'
alias st='python manage.py collectstatic'  
""" 
 