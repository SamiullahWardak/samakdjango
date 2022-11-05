from django.urls import reverse
from email.policy import default
from multiprocessing.dummy import active_children
from unittest.util import _MAX_LENGTH
from django.db import models

class Article(models.Model):
    title   = models.CharField(max_length = 40)
    content = models.TextField()
    active  = models.BooleanField(default = True)
    
    def get_absolute_url(self):
        return reverse('articles:article-detail', kwargs={"pk": self.pk})
    