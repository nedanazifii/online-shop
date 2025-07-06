from django.db import models
from django.contrib.auth.models import User



class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_full_name = models.CharField(max_length=100)
    shipping_email = models.EmailField(max_length=100)
    shipping_phone = models.CharField(max_length=25, blank=True)
    shipping_address1 = models.CharField(max_length=400, blank=True)
    shipping_address2 = models.CharField(max_length=400, blank=True)
    shipping_city = models.CharField(max_length=30, blank=True)
    shipping_state = models.CharField(max_length=30, blank=True)
    shipping_zipcode = models.CharField(max_length=30, blank=True)
    shipping_country = models.CharField(max_length=30, default="IRAN", null=True, blank=True)
    shipping_old_cart = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'Shipping Address From {self.shipping_full_name}'
