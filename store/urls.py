from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_info/', views.update_info, name='update_info'),
    path('product/<int:product_id>', views.product_detail, name='product'),
    path('products/', views.all_product_list, name='products'),
    path('category/<str:category_name>', views.category, name='category'),
    path('search/', views.search, name='search'),
    path('orders/', views.user_orders, name='orders'),
    path('order_details/<int:order_id>', views.order_details, name='order_details'),
]
