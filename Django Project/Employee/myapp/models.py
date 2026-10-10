from django.db import models

# Create your models here.

class EmployeeList(models.Model):
    Name = models.CharField(max_length=50)
    Role = models.CharField(max_length=50)

    def __str__ (self):
        return self.Name

class ShiftList(models.Model):
    employee = models.ForeignKey(EmployeeList,on_delete=models.CASCADE)
    StartTime = models.TimeField(auto_now=False, auto_now_add=False)
    EndTime = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__ (self):
        return str(self.StartTime)