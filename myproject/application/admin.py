from django.contrib import admin

from .models import Blog, Fruit

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ['name']

