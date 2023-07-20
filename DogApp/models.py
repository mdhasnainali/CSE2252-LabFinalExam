from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class DogShop(models.Model):
    name = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    price = models.IntegerField()
    breed = models.CharField(max_length=30,validators=[MinLengthValidator(3)])
    description = models.CharField(max_length=100,validators=[MinLengthValidator(10)])

    def __str__(self):
        return self.name