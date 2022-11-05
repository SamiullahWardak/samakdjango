from distutils.command.upload import upload
from email.policy import default
import imghdr
from django.db import models


class Destenation(models.Model):
    name = models.CharField(max_length=40)
    img  = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=False)
    