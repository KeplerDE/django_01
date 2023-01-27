from django.contrib import admin

from my_site.models import Articles

from my_site.models import Absolute

# Register your models here.

@admin.register(Absolute)
class AbsoluteAdmin(admin.ModelAdmin):
    list_display=['name', 'slug', 'created']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ["title",]
    prepopulated_fields = {"slug": ("title",)}
    
    
   