from django.db import models

# Create your models here.

class produts(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='database/') #--> python -m pip install Pillow

    def __str__(self):
        return self.name
    



