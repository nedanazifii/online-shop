from django.contrib import admin
from . import models
from django.contrib.auth.models import User


class ProfileInLine(admin.StackedInline):
    model = models.Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInLine]


class SubFeatureInline(admin.TabularInline):
    model = models.SubFeature
    extra = 1


class FeatureAdmin(admin.ModelAdmin):
    inlines = [SubFeatureInline]


class ProductFeatureValueInline(admin.TabularInline):
    model = models.ProductFeatureValue
    extra = 1

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super().formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'subfeature' and request._obj_ is not None:
            field.queryset = field.queryset.filter(feature__category=request._obj_.category)
        return field


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_sale', 'sale_price', 'star']
    inlines = [ProductFeatureValueInline]

    def get_form(self, request, obj=None, **kwargs):
        request._obj_ = obj
        return super().get_form(request, obj, **kwargs)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(models.Category)
admin.site.register(models.Feature, FeatureAdmin)
admin.site.register(models.Customer)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Profile)
