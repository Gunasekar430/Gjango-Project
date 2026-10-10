from django.db import models

# Create your models here.

class DeliveryEmployee(models.Model):
    name = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    current_Orders = models.IntegerField(default=0)
    status = models.CharField(default='Free', max_length=50)

    def __str__(self):
        return self.name

class Order(models.Model):
    order = models.ForeignKey(DeliveryEmployee, on_delete=models.CASCADE)
    customer_name = models.CharField( max_length=50)
    address = models.CharField( max_length=50)
    priority = models.CharField( max_length=50)
    assigned_to = models.CharField( max_length=50)
    status = models.CharField( max_length=50)

    def __str__(self):
        return self.customer_name

