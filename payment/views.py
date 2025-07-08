from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from .forms import ShippingForm
from .models import ShippingAddress, Order, OrderItem
from django.contrib import messages
from store.models import Product
from django.contrib.auth.models import User


def payment(request):
    return render(request, 'payment/payment.html')


def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_products()
    quantities = cart.get_quantities()
    total = cart.get_total()

    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
    else:
        shipping_form = ShippingForm(request.POST or None)

    return render(request, 'payment/checkout.html',
                  {'cart_products': cart_products, 'quantities': quantities, 'total': total,
                   'shipping_form': shipping_form})


def confirm_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_products()
        quantities = cart.get_quantities()
        total = cart.get_total()

        user_shipping = request.POST
        request.session['user_shipping'] = user_shipping

        return render(request, 'payment/confirm_order.html',
                      {'cart_products': cart_products, 'quantities': quantities, 'total': total,
                       'user_shipping': user_shipping})
    else:
        messages.success(request, 'دسترسی به این صفحه امکان پذیر نمی باشد')
        return redirect('home')


def process_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_products()
        quantities = cart.get_quantities()
        total = cart.get_total()

        user_shipping = request.session.get('user_shipping')

        full_name = user_shipping["shipping_full_name"]
        email = user_shipping["shipping_email"]
        full_address = f'{user_shipping["shipping_address1"]}\n{user_shipping["shipping_address2"]}\n{user_shipping["shipping_city"]}\n{user_shipping["shipping_state"]}\n{user_shipping["shipping_zipcode"]}\n{user_shipping["shipping_country"]}'

        if request.user.is_authenticated:
            user = request.user
            new_order = Order(user=user, full_name=full_name, email=email, shipping_address=full_address,
                              amount_paid=total)
            new_order.save()

            odr = get_object_or_404(Order, id=new_order.pk)
            for product in cart_products:
                prod = get_object_or_404(Product, id=product.id)

                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price

                for key, value in quantities.items():
                    if int(key) == product.id:
                        new_item = OrderItem(order=odr, product=product, price=price, quantity=value, user=user)
                        new_item.save()

            messages.success(request, 'سفارش ثبت شد')
            return redirect('home')

        else:
            new_order = Order(full_name=full_name, email=email, shipping_address=full_address,
                              amount_paid=total)
            new_order.save()
            odr = get_object_or_404(Order, id=new_order.pk)
            for product in cart_products:
                prod = get_object_or_404(Product, id=product.id)

                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price

                for key, value in quantities.items():
                    if int(key) == product.id:
                        new_item = OrderItem(order=odr, product=product, price=price, quantity=value)
                        new_item.save()

            messages.success(request, 'سفارش ثبت شد')
            return redirect('home')
    else:
        messages.success(request, 'دسترسی به این صفحه امکان پذیر نمی باشد')
        return redirect('home')
