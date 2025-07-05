import json
from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, UpdateUserForm, UpdatePasswordForm, UpdateUserInfo
from django.db.models import Q
from cart.cart import Cart


def product_list(request):
    all_products = Product.objects.all()[:6]
    return render(request, 'index.html', {'products': all_products})


def all_product_list(request):
    all_products = Product.objects.all()
    return render(request, 'products.html', {'products': all_products})


def about(request):
    return render(request, 'about.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            current_user = Profile.objects.get(user__id=request.user.id)
            saved_cart = current_user.old_cart
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

            messages.success(request, "با موفقیت وارد شدید", 'success')
            return redirect('home')
        else:
            messages.warning(request, "نام یا رمز اشتباه", 'warning')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "با موفقیت خارج شدید", 'success')
    return redirect('home')


def signup_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            messages.success(request, "حساب کاربری شما ساخته شد", 'success')
            return redirect('update_info')
        else:
            messages.warning(request, 'مشکلی در ثبت نام وجود دارد', 'warning')
            return redirect('signup')

    else:
        return render(request, 'signup.html', {'form': form})


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, 'اطلاعات ویرایش شد')
            return redirect('home')

        return render(request, 'update_user.html', {'user_form': user_form})
    else:
        messages.success(request, 'ابتدا باید وارد حساب کاربری خود شوید')
        return redirect('home')


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user

        if request.method == 'POST':
            form = UpdatePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'رمز عبور ویرایش شد')
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.success(request, error)
                return redirect('update_user')

        else:
            form = UpdatePasswordForm(current_user)
            return render(request, 'update_password.html', {'form': form})
    else:
        messages.success(request, 'ابتدا باید وارد حساب کاربری خود شوید')
        return redirect('home')


def update_info(request):
    if request.user.is_authenticated:
        # current_user = Profile.objects.get(user__id=request.user.id)
        current_user, created = Profile.objects.get_or_create(user=request.user)
        form = UpdateUserInfo(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'اطلاعات کاربری ویرایش شد')
            return redirect('home')

        return render(request, 'update_info.html', {'form': form})
    else:
        messages.success(request, 'ابتدا باید وارد حساب کاربری خود شوید')
        return redirect('home')



def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product.html', {'product': product})


def category(request, category_name):
    category_name = category_name.replace('-', ' ')
    try:
        category = Category.objects.get(name=category_name)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})

    except:
        messages.success(request, "دسته بندی وجود ندارد", 'success')
        return redirect('home')


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))

        if not searched:
            messages.success(request, "محصولی وجود ندارد", 'success')
            return render(request, 'search.html')
        else:
            return render(request, 'search.html', {'searched': searched})

    return render(request, 'search.html')

