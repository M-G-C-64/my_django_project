
from django.db import models

# Create your models here.

class F1car(models.Model):
    car = models.CharField(max_length=20, unique = True)
    Constructors = models.IntegerField()
    Current_Driver = models.CharField(max_length = 30)
    Best_Driver = models.CharField(max_length = 30)

class Topic(models.Model):
    top_name = models.CharField(max_length = 64, unique = True)

    def __str__(self) -> str:
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, default ="null", on_delete = models.SET_DEFAULT)
    name = models.CharField(max_length = 64, unique = True)
    url = models.URLField(unique = True)

    def __str__(self) -> str:
        return self.name

class AccessRecords(models.Model):
    name = models.ForeignKey(Webpage, default = "null", on_delete = models.SET_DEFAULT)
    date = models.DateField()
