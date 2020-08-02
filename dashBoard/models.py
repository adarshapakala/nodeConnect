from django.db import models

# Create your models here.
class Platforms(models.Model):
    name = models.CharField(max_length=10, unique=True)

class Catogeries(models.Model):
    name = models.CharField(max_length=10, unique=True)

class Questions(models.Model):
    platform = models.ForeignKey(Platforms, on_delete=models.CASCADE)
    catogery = models.ForeignKey(Catogeries, on_delete=models.CASCADE)
    qStatement = models.TextField()
    qDescritpion = models.TextField()
    qNote = models.TextField()
    picture = models.ImageField(upload_to ='pics')




