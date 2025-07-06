from django.db import models
from django.contrib.auth.models import User



class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=25, blank=True)
    address1 = models.CharField(max_length=400, blank=True)
    address2 = models.CharField(max_length=400, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    zipcode = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, default="IRAN")
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'Shipping Address From {self.full_name}'
