from django.db import models


class Language(models.Model):
    english = models.CharField(max_length=250, blank=True, default='')
    russian = models.CharField(max_length=250, blank=True, default='')
    turkmen = models.CharField(max_length=250, blank=True, default='')
    turkish = models.CharField(max_length=250, blank=True, default='')

    class Meta:
        ordering = ('english',)