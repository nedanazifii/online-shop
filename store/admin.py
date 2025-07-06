# from django.contrib import admin
# from . import models
# from django.contrib.auth.models import User
#
# admin.site.register(models.Category)
# admin.site.register(models.Customer)
# admin.site.register(models.Product)
# # admin.site.register(models.Order)
# admin.site.register(models.Profile)
#
#
# class ProfileInLine(admin.StackedInline):
#     model = models.Profile
#
# class UserAdmin(admin.ModelAdmin):
#     model = User
#     fields = ['username', 'first_name', 'last_name', 'email']
#     inlines = [ProfileInLine]
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

from django.contrib import admin
from . import models
from django.contrib.auth.models import User

# ثبت Profile درون صفحه User
class ProfileInLine(admin.StackedInline):
    model = models.Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInLine]

# ثبت ویژگی‌ها در صفحه Product
class ProductFeatureInline(admin.TabularInline):
    model = models.ProductFeature
    extra = 1  # تعداد ویژگی‌های جدید قابل اضافه

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_sale', 'sale_price', 'star']
    inlines = [ProductFeatureInline]

# ثبت مدل‌ها
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(models.Category)
admin.site.register(models.Customer)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Profile)

