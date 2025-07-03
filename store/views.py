from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm


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
            return redirect('home')
        else:
            messages.warning(request, 'مشکلی در ثبت نام وجود دارد', 'warning')
            return redirect('signup')

    else:
        return render(request, 'signup.html', {'form': form})


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
