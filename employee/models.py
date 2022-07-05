from django.db import models

# Create your models here.
class Employee(models.Model):
    emplyee_name = models.TextField()
    employee_email = models.TextField()
    employee_address = models.TextField(null=True)