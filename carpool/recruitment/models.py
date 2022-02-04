from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.
class Recruit(models.Model):
    departure = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    car_num = models.CharField(max_length=10)
    time = models.CharField(max_length=100)
    max_num = models.IntegerField(blank=True, null=True)
    present_num = models.PositiveIntegerField()
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        str = self.departure + ' => ' + self.destination
        return str