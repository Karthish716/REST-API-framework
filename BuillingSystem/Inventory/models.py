from django.db import models

# Create your models here.
class Products(models.Model):

    products_name = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=0)

    def __str__(self):

        return self.products_name