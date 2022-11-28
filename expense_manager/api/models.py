from django.db import models

class Category(models.Model):
    type = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    class Meta:
        ordering  = ['type']
