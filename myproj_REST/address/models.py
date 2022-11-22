from django.db import models


# Create your models here.
class Address(models.Model):
    first_name=models.CharField(max_length=50)
    second_name=models.CharField(max_length=50)
    email_name=models.EmailField(max_length=30)
    phone_name= models.CharField(max_length=10)