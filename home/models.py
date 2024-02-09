from django.db import models
from django.contrib.auth.models import User


class registration(models.Model):
    User=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    full_name=models.CharField(max_length=200)
    fathers_name=models.CharField(max_length=200)
    gender=models.ChoiceField(max_length=200)
    email=models.CharField(max_length=200,unique=True)
    password=models.TextField()
    address1=models.TextField()
    address2=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.IntegerField()

class lo(models.Model):
    username=models.CharField(max_length=200)  
    
