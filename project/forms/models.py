from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse



class Inform(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField()
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='informs')
    added_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('an_search', args=[str(self.id)])


class Category(models.Model):
    NEWS = "News"
    ARTICLES = 'Articles'

    fields = ([NEWS, 'News'],
                [ARTICLES, "Articles"])
    category = models.CharField(max_length=100, choices= fields, unique=True, default='News')

    def __str__(self):
        return self.category

