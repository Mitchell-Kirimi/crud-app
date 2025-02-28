from django.db import models

# Create your models here.
class User (models.Model):
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='upload',default="a.png")
    Email =models.EmailField(unique=True)
    password = models.CharField(max_length=70)
    date_of_birth = models.CharField(max_length=10)
    def __str__(self):
        return self.name
