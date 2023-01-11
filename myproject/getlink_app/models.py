from django.db import models

class Page(models.Model):
    class Meta:
        verbose_name = "Страница id, slug, namespace"
        verbose_name_plural = "Страницы id, slug, namespace"

    name = models.CharField(max_length=160)
    content = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
