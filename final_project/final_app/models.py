from django.db import models


# Create your models here.
class store(models.Model):
    name = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name