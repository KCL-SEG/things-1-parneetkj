from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(name, description, quantity):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
        )
