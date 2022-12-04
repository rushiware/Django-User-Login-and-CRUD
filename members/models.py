from django.db import models

# Create your models here.
class Members(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)

class Login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)