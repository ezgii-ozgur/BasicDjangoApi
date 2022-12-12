from django.db import models


class Students(models.Model):
    StudentId = models.AutoField(primary_key=True)
    StudentName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    Date = models.DateField()
    PhotoFileName = models.CharField(max_length=500)
