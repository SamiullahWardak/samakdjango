import email
from email.policy import default
from msilib.schema import MsiAssemblyName
from typing_extensions import Required
from django.db import models

# Create your models here.

class product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=100)
    summary     = models.TextField(default="this is cool!")
    featured    = models.BooleanField(default=True)
    myName      = models.CharField(max_length=25)