from django.db import models


class Product(models.Model):
    sku = models.CharField(max_length=13, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=250, null=False, blank=False)
    price = models.FloatField(null=False)
    height = models.FloatField(null=False)
    width = models.FloatField(null=False)
    length = models.FloatField(null=False)
    weight = models.FloatField(null=False)

    def __str__(self):
        return f'{self.name} - {self.sku}'
