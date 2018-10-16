from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CHOICES=(('Mr','Mr.'),('Mrs','Mrs.'))
class Member_Details(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    title=models.CharField(max_length=3,choices=CHOICES)
    first_Name=models.CharField(max_length=20)
    last_Name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    DOB=models.DateField()
