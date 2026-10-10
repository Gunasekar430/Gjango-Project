from django.db import models

# Create your models here.

class Products(models.Model):
    
    name = models.CharField( max_length=50)
    category = models.CharField( max_length=50)
    quantity = models.IntegerField(default=0)
    minimum_stock = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class RestockRequests(models.Model):
    Choice_status =[ 
        { 'Pending' , 'Pending' },
        { 'Approve', 'Approve' },
        { 'Reject', 'Reject' }
    ]

    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    status = models.CharField(Choice_status, default= 'Pending',max_length=50)
    requested_quantity = models.IntegerField(default=0)
    created_at = models.TimeField( auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.status