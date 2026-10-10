from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=100)

    category = models.CharField(max_length=100)

    quantity = models.IntegerField(default=0)

    minimum_stock = models.IntegerField(default=0)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class RestockRequest(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    requested_quantity = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name