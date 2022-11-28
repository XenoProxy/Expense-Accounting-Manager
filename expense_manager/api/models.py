from django.db import models

class Category(models.Model):
    type = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='category', on_delete=models.CASCADE)
    class Meta:
        ordering  = ['type']
