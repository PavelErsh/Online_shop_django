from django.db import models

# Create your models here.
class Item (models.Model):
    name = models.CharField(max_length=120)
    color = models.CharField(max_length=120)
    price = models.IntegerField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

   