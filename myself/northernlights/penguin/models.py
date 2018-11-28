from django.db import models

# Create your models here.
class Goods(models.Model):
    item = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)