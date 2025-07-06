from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'full name'}),
        required=True
    )

    shipping_email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
        required=True
    )

    shipping_phone = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
        required=True
    )

    shipping_address1 = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address 1 '}),
        required=True
    )

    shipping_address2 = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address 2 '}),
        required=False
    )

    shipping_city = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city '}),
        required=True
    )

    shipping_state = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'state '}),
        required=True
    )

    shipping_zipcode = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zipcode '}),
        required=False
    )
    shipping_country = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'country '}),
        required=False
    )

    class Meta:
        model = ShippingAddress
        fields = ('shipping_full_name', 'shipping_email', 'shipping_phone', 'shipping_address1', 'shipping_address2',
                  'shipping_city', 'shipping_state', 'shipping_zipcode', 'shipping_country')

        exclude = ['user',]
