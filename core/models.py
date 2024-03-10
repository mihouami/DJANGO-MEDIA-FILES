from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='dogs/')