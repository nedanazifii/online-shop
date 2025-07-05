from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus', None)

    first_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}),
                error_messages={
            'required': 'لطفاً نام خود را وارد کنید.',
            'max_length': 'نام نباید بیش از ۲۰ کاراکتر باشد.'
        }
    )

    last_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'}),
        error_messages={
            'required': 'لطفاً نام خانوادگی خود را وارد کنید.',
            'max_length': 'نام خانوادگی نباید بیش از ۲۰ کاراکتر باشد.'
        }
    )

    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'}),
        error_messages={
        'required': 'لطفاً ایمیل خود را وارد کنید.',
        'invalid': 'لطفاً یک ایمیل معتبر وارد کنید.'
    }
    )

    username = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری '}),
        error_messages={
            'required': 'لطفاً نام کاربری را وارد کنید.',
            'max_length': 'نام کاربری نباید بیش از ۲۰ کاراکتر باشد.'
        }
    )

    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'name': 'password',
                'type': 'password',
                'placeholder': 'رمز عبور'

            }
        ),
        error_messages={
            'required': 'لطفاً رمز عبور را وارد کنید.'
        }
    )

    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'name': 'password',
                'type': 'password',
                'placeholder': 'تکرار رمز عبور'
            }
        ),
        error_messages={
           'required': 'لطفاً تکرار رمز عبور را وارد کنید.'
        }
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class UpdateUserForm(UserChangeForm):
    password = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus', None)

    first_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}),
        required=False
    )

    last_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'}),
        required=False  
    )

    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'}),
        required=False
    )

    username = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری '}),
        required=False
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'name': 'password',
                'type': 'password',
                'placeholder': 'رمز عبور جدید'

            }
        )
    )

    new_password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'name': 'password',
                'type': 'password',
                'placeholder': 'تکرار رمز عبور'
            }
        )
    )

    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')


class UpdateUserInfo(forms.ModelForm):
    phone = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تلفن'}),
        required = False
    )
    address1 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس اول'}),
        required=False
    )
    address2 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس دوم'}),
        required=False
    )
    city = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شهر'}),
        required=False
    )
    state = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'استان'}),
        required=False
    )
    zipcode = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کد پستی'}),
        required=False
    )
    country = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کشور'}),
        required=False
    )
    class Meta:
        model = Profile
        fields = ('phone', 'address1', 'address2','city', 'state', 'zipcode', 'country')
