from django.db import models


# Create your models here.

class Category(models.Model):
    select = models.CharField(max_length=30)

    def __str__(self):
        return self.select


class Money(models.Model):
    description = models.CharField(max_length=255)
    select = models.CharField(max_length=30)
    revenue = models.BooleanField(True)
    expense = models.BooleanField(False)
    date = models.DateField
    amount = models.FloatField
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.select
