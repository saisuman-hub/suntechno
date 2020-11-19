from django.db import models


# Create your models here.
class Userinfo(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100,unique=True)
    email_id= models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    re_enter = models.CharField(max_length=100)

class Booking_info(models.Model):
    checkin = models.DateTimeField(default=False)
    checkout = models.DateTimeField(default=False)
    singleBHK = models.BooleanField()
    doubleBHK = models.BooleanField()