from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True)
    # tags = models.TextField(null=True)
    tags = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)