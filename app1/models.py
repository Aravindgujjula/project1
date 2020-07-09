from django.db import models

# Create your models here.
class course(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    faculty = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    time = models.CharField(max_length=50)
    fee = models.FloatField()
    duration = models.CharField(max_length=30)
