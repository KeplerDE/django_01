from django.contrib import admin

from .models import Blog, Fruit, Articles

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ['name']




@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ["title",]
    prepopulated_fields = {"slug": ("title",)}