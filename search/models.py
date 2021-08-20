from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    desc = models.TextField()
    stock = models.CharField(max_length=50)
    def __str__(self):
        return self.name