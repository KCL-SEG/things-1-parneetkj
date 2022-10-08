from django.db import models

class Thing():
    name = models.CharField()
    description = models.CharField()
    quantity = models.IntegerField()
