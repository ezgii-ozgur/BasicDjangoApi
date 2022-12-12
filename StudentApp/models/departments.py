from django.db import models


class Departments(models.Model):
    Department_id = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)