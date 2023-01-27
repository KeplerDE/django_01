from django.db import models
from django.urls import reverse
class Page(models.Model):
    class Meta:
        verbose_name = "Страница id, slug, namespace"
        verbose_name_plural = "Страницы id, slug, namespace"

    name = models.CharField(max_length=160)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=50,
                            db_index=True,
                            unique=True)
    data_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('yes_ns:detail_absolute_path', kwargs={'id': self.id, 'slug': self.slug})    # теперь он знает что возвращать
    # идёт пряиое обрашение
    # def get_absolute_url(self):
    #     return f"/page/absolute-path/{self.id}/{self.slug}/detail/"
