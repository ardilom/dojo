from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField('name', max_length=250)
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return "<product: {} -- qty: {}>".format(self.name, self.quantity)