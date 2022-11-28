from django.db import models

class Category(models.Model):
    type = models.CharField(max_length=100, blank=True, default='')
    class Meta:
        ordering  = ['type']
