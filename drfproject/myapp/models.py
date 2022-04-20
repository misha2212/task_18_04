from django.db import models

# Create your models here.


class CategoriesOfProducts(models.Model):
    name = models.CharField(max_length=255)
    seq = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class GroupsOfProducts(models.Model):
    category_id = models.ForeignKey('CategoriesOfProducts', on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    seq = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    group_id = models.ForeignKey('GroupsOfProducts', on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    hidden = models.BooleanField(default=True)

    def __str__(self):
        return self.name
