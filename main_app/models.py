from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

DONATIONS= (
    ('F', 'Food'),
    ('H', 'Health'),
    ('T', 'Training'),
    ('O', 'Other')
)

class Resource(models.Model):
    type = models.CharField(max_length=50, choices=DONATIONS, default=DONATIONS[0][0])
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    species = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('index')


class Comment(models.Model):
  date = models.DateField('comment date')
  content = models.TextField( max_length=200)
  resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
     return f"{self.content} on {self.date}"
