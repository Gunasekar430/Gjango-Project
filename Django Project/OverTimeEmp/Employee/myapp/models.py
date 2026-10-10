from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField( max_length=50)

    def __str__(self):
        return self.name

class Shift(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    employee_id = models.CharField( max_length=50)
    start_time = models.TimeField( auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        shift = Shift.objects.all()
        
        return self.employee_id