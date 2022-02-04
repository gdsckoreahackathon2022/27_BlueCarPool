from django.db import models

class Report(models.Model):
    subject=models.CharField(max_length=100)
    car_num=models.CharField(max_length=10)
    content=models.TextField()
    create_date=models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    report=models.ForeignKey(Report,on_delete=models.CASCADE)
    content=models.TextField()
    create_date=models.DateTimeField()