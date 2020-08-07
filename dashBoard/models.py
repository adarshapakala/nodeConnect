from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class Platforms(models.Model):
    name = models.CharField(max_length=5, unique=True)
    def __str__(self):
        return self.name

class Catogeries(models.Model):
    name = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return self.name

class Questions(models.Model):
    platform_FK = models.ForeignKey(Platforms, on_delete=models.CASCADE)
    catogery_FK = models.ForeignKey(Catogeries, on_delete=models.CASCADE)
    qStatement = models.TextField()
    qDescritpion = models.TextField()
    qNote = models.TextField()
    picture = models.ImageField(upload_to ='pics', blank=True, null=True)
    qNumber=models.IntegerField()
    templatePath = models.FileField(upload_to='qTemplate', blank=True, null=True)

    def __str__(self):
        return "Platform:" + str(self.platform_FK) + " Catogery:" + str(self.catogery_FK) + " Q:" + self.qStatement


class QuestionGroup(models.Model):
    name = models.CharField(max_length=30, unique=True)
    platform_FK = models.ForeignKey(Platforms, on_delete=models.CASCADE)
    catogery_FK = models.ForeignKey(Catogeries, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class UserCurrentQuestion(models.Model):    
    user_FK = models.ForeignKey(User, on_delete=models.CASCADE)
    question_FK = models.ForeignKey(QuestionGroup, on_delete=models.CASCADE)
    questionNumber_FK = models.IntegerField(default=0)
    def __str__(self):
        return "User:" + str(self.user_FK) + " Question FK:" + str(self.question_FK)



