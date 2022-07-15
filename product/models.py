from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)


class Category(models.Model):
    category_name = models.CharField(max_length=150)
