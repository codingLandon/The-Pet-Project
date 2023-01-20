from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class Resource(models.Model):
    type = models.CharField(max_length=10)
    description = models.TextField(max_length=250)
    location = models.TextField(max_length=250)
    species = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('index')