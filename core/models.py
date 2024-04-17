from django.db import models

# Create your models here.

class Coffe(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='coffe_images/')


    