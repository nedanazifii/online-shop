from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile
import re


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus', None)

    first_name = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}),
        error_messages={
            'required': 'لطفاً نام خود را وارد کنید.',
            'max_length': 'نام نباید بیش از ۲۰ کاراکتر باشد.'
        }
    )

    last_name = forms.CharField(
        label='',
        max_length=20,
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

    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        if not password:
            raise forms.ValidationError('لطفا رمز عبور را وارد کنید.')

        if len(password) < 8:
            raise forms.ValidationError('رمز عبور باید حداقل ۸ کاراکتر باشد.')

        if not any(char.isdigit() for char in password):
            raise forms.ValidationError('رمز عبور باید شامل حداقل یک عدد باشد.')

        if not any(char.isalpha() for char in password):
            raise forms.ValidationError('رمز عبور باید شامل حداقل یک حرف باشد.')

        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("رمزهای عبور مطابقت ندارند.")

        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('این نام کاربری قبلاً ثبت شده است. لطفاً نام دیگری انتخاب کنید.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل قبلاً ثبت شده است. لطفاً ایمیل دیگری وارد کنید.')
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not re.match(r'^[آ-یa-zA-Z\s]+$', first_name):
            raise forms.ValidationError('نام فقط باید شامل حروف باشد.')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not re.match(r'^[آ-یa-zA-Z\s]+$', last_name):
            raise forms.ValidationError('نام خانوادگی فقط باید شامل حروف باشد.')
        return last_name

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


# class UpdateUserForm(UserChangeForm):
#     password = None
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.pop('autofocus', None)
#
#     first_name = forms.CharField(
#         label='',
#         max_length=50,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}),
#         required=False
#     )
#
#     last_name = forms.CharField(
#         label='',
#         max_length=50,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'}),
#         required=False
#     )
#
#     email = forms.EmailField(
#         label='',
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'}),
#         required=False
#     )
#
#     username = forms.CharField(
#         label='',
#         max_length=20,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری '}),
#         required=False
#     )
#
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'username')
#

class UpdateUserForm(UserChangeForm):
    password = None  # حذف فیلد پسورد

    first_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}),
        required=False,
        error_messages={
            'max_length': 'نام نباید بیش از ۵۰ کاراکتر باشد.'
        }
    )

    last_name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'}),
        required=False,
        error_messages={
            'max_length': 'نام خانوادگی نباید بیش از ۵۰ کاراکتر باشد.'
        }
    )

    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'}),
        required=False,
        error_messages={
            'invalid': 'لطفاً یک ایمیل معتبر وارد کنید.'
        }
    )

    username = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}),
        required=False,
        error_messages={
            'max_length': 'نام کاربری نباید بیش از ۲۰ کاراکتر باشد.'
        }
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('این ایمیل قبلاً ثبت شده است.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('این نام کاربری قبلاً گرفته شده است.')
        return username

# class UpdatePasswordForm(SetPasswordForm):
#     new_password1 = forms.CharField(
#         label='',
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'name': 'password',
#                 'type': 'password',
#                 'placeholder': 'رمز عبور جدید'
#
#             }
#         )
#     )
#
#     new_password2 = forms.CharField(
#         label='',
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 'name': 'password',
#                 'type': 'password',
#                 'placeholder': 'تکرار رمز عبور'
#             }
#         )
#     )
#
#     class Meta:
#         model = User
#         fields = ('new_password1', 'new_password2')
class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور جدید'}),
        error_messages={
            'required': 'لطفاً رمز عبور جدید را وارد کنید.'
        }
    )

    new_password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تکرار رمز عبور'}),
        error_messages={
            'required': 'لطفاً تکرار رمز عبور را وارد کنید.'
        }
    )

    def clean_new_password1(self):
        password = self.cleaned_data.get('new_password1')
        if not password:
            raise forms.ValidationError('لطفاً رمز عبور جدید را وارد کنید.')
        if len(password) < 8:
            raise forms.ValidationError('رمز عبور باید حداقل ۸ کاراکتر باشد.')
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError('رمز عبور باید شامل حداقل یک عدد باشد.')
        if not any(char.isalpha() for char in password):
            raise forms.ValidationError('رمز عبور باید شامل حداقل یک حرف باشد.')
        return password


# class UpdateUserInfo(forms.ModelForm):
#     phone = forms.CharField(
#         label='',
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تلفن'}),
#         required=False
#     )
#     address1 = forms.CharField(
#         label='',
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس اول'}),
#         required=False
#     )
#     address2 = forms.CharField(
#         label='',
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس دوم'}),
#         required=False
#     )
#     city = forms.CharField(
#         label='',
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شهر'}),
#         required=False
#     )
#     state = forms.CharField(
#         label='',
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'استان'}),
#         required=False
#     )
#     zipcode = forms.CharField(
#         label='',
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کد پستی'}),
#         required=False
#     )
#     country = forms.CharField(
#         label='',
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کشور'}),
#         required=False
#     )
#
#     class Meta:
#         model = Profile
#         fields = ('phone', 'address1', 'address2', 'city', 'state', 'zipcode', 'country')
class UpdateUserInfo(forms.ModelForm):
    phone = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تلفن'}),
        required=False
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
        fields = ('phone', 'address1', 'address2', 'city', 'state', 'zipcode', 'country')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            pattern = r'^\+?[\d\s-]{7,15}$'
            if not re.match(pattern, phone):
                raise forms.ValidationError('شماره تلفن معتبر نیست.')
        return phone

    def clean_zipcode(self):
        zipcode = self.cleaned_data.get('zipcode')
        if zipcode:
            if not zipcode.isdigit():
                raise forms.ValidationError('کد پستی باید فقط شامل عدد باشد.')
        return zipcode

    def clean_country(self):
        country = self.cleaned_data.get('country')
        if country and len(country) > 50:
            raise forms.ValidationError('نام کشور نباید بیش از ۵۰ کاراکتر باشد.')
        return country

    def clean_city(self):
        city = self.cleaned_data.get('city')
        if city and len(city) > 50:
            raise forms.ValidationError('نام شهر نباید بیش از ۵۰ کاراکتر باشد.')
        return city

    def clean_state(self):
        state = self.cleaned_data.get('state')
        if state and len(state) > 50:
            raise forms.ValidationError('نام استان نباید بیش از ۵۰ کاراکتر باشد.')
        return state


