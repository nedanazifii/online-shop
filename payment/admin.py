from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem

admin.site.register(ShippingAddress)
admin.site.register(OrderItem)


class OrderItemLine(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['date_ordered', 'last_update']
    inlines = [OrderItemLine]
