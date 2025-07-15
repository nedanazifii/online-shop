from django import forms
from .models import ShippingAddress
import re


class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'full name'}),
        required=True,
        error_messages={
            'required': 'لطفاً نام را وارد کنید.',
            'max_length': 'نام نباید بیش از ۵۰ کاراکتر باشد.'
        }
    )

    shipping_email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
        required=True,
        error_messages={
            'required': 'لطفاً ایمیل را وارد کنید.',
            'invalid': 'لطفاً یک ایمیل معتبر وارد کنید.'
        }
    )

    shipping_phone = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
        required=True,
        error_messages={
            'required': 'لطفاً شماره تلفن را وارد کنید.',
            'max_length': 'شماره تلفن نباید بیش از ۲۰ رقم باشد.'
        }
    )

    shipping_address1 = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address 1 '}),
        required=True,
        error_messages={
            'required': 'آدرس اول الزامی است.',
            'max_length': 'آدرس نباید بیش از ۱۰۰ کاراکتر باشد.'
        }
    )

    shipping_address2 = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address 2 '}),
        required=False,
        error_messages={
            'max_length': 'آدرس نباید بیش از ۱۰۰ کاراکتر باشد.'
        }
    )

    shipping_city = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city '}),
        required=True,
        error_messages={
            'required': 'شهر الزامی است.',
            'max_length': 'نام شهر نباید بیش از ۵۰ کاراکتر باشد.'
        }
    )

    shipping_state = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'state '}),
        required=True,
        error_messages={
            'required': 'استان الزامی است.',
            'max_length': 'نام استان نباید بیش از ۵۰ کاراکتر باشد.'
        }
    )

    shipping_zipcode = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zipcode '}),
        required=False,
        error_messages={
            'max_length': 'کد پستی نباید بیش از ۲۰ رقم باشد.'
        }
    )
    shipping_country = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'country '}),
        required=False,
        error_messages={
            'max_length': 'نام کشور نباید بیش از ۵۰ کاراکتر باشد.'
        }
    )

    class Meta:
        model = ShippingAddress
        fields = ('shipping_full_name', 'shipping_email', 'shipping_phone', 'shipping_address1', 'shipping_address2',
                  'shipping_city', 'shipping_state', 'shipping_zipcode', 'shipping_country')

        exclude = ['user',]

    def clean_shipping_phone(self):
        phone = self.cleaned_data.get('shipping_phone')
        if phone:
            pattern = r'^\+?[\d\s\-]{7,15}$'
            if not re.match(pattern, phone):
                raise forms.ValidationError('شماره تلفن وارد شده معتبر نیست.')
        return phone

    def clean_shipping_zipcode(self):
        zipcode = self.cleaned_data.get('shipping_zipcode')
        if zipcode and not zipcode.isdigit():
            raise forms.ValidationError('کد پستی باید فقط شامل عدد باشد.')
        return zipcode

    def clean_shipping_country(self):
        country = self.cleaned_data.get('shipping_country')
        if country and len(country) > 50:
            raise forms.ValidationError('نام کشور نباید بیش از ۵۰ کاراکتر باشد.')
        return country

    def clean_shipping_city(self):
        city = self.cleaned_data.get('shipping_city')
        if city and len(city) > 50:
            raise forms.ValidationError('نام شهر نباید بیش از ۵۰ کاراکتر باشد.')
        return city

    def clean_shipping_state(self):
        state = self.cleaned_data.get('shipping_state')
        if state and len(state) > 50:
            raise forms.ValidationError('نام استان نباید بیش از ۵۰ کاراکتر باشد.')
        return state
