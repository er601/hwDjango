from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)


class Category(models.Model):
    category_name = models.CharField(max_length=150)


class Price(models.Model):
    type = models.CharField(max_length=10)
    description = models.TextField()
    support = models.BooleanField(default=False)
    duration = models.PositiveIntegerField(default=30)
    storage = models.IntegerField(default=10)
    price = models.IntegerField()
