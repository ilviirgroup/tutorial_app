from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    english = models.CharField(max_length=250, blank=True, default='')
    russian = models.CharField(max_length=250, blank=True, default='')
    turkmen = models.CharField(max_length=250, blank=True, default='')
    turkish = models.CharField(max_length=250, blank=True, default='')
    color = models.CharField(max_length=250, blank=True, default='')

    class Meta:
        ordering = ('english',)