from django.db import models

# Create your models here.
from django.db import models


class Cache(models.Model):
    bookid= models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    topic = models.CharField(max_length=200)
    def __str__(self):
        return self.title



