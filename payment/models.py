from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.db.models.signals import post_save


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

def create_shipping_user(sender, instance, created, **kwargs):
    if created:
        user_shipping = ShippingAddress(user=instance)
        user_shipping.save()

post_save.connect(create_shipping_user,sender=User)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    shipping_address = models.TextField(max_length=150000)
    amount_paid = models.DecimalField(decimal_places=0, max_digits=12)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order str({self.id})'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(decimal_places=0, max_digits=12)

    def __str__(self):
        return f'Order Item str({self.id})'
