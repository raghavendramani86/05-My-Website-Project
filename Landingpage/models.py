from django.db import models
from django.contrib.auth.models import User #this is the user class of django

# Create your models here.

class Profile(models.Model):
    # this will inherit all the user class attributes
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # additional attributes are added here
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='user_pics',blank=True)

class Details(models.Model):
    Age = models.IntegerField()
    sex = models.CharField(max_length=1,choices = [('M','Male'),('F','Female'),('O','Other')])
