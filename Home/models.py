from django.db import models

# Create your models here.
#these are SQL of a database

class Image(models.Model):
    image=models.ImageField(upload_to="myimage")
    date=models.DateTimeField(auto_now_add=True)
