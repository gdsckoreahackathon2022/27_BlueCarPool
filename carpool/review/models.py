from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Review(models.Model):
    subject = models.CharField(max_length=200)
    car_num = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject