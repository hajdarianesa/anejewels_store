"""
URL configuration for anejewels_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from anejewels.views import home,product_detail,product_list,cart,add_to_cart,remove_from_cart, register, add_product,logout_view,login_view,payment,submit_payment,confirm,paypal
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
     path('categories/<int:category_id>/products/', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', cart, name='cart'),
    path('add-to-cart/<int:product_id>/',add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('add-product/', add_product, name='add_product'),
    path('logout/', logout_view, name='logout'),
    path('payment/', payment, name='payment'),
    path('submit_payment/', submit_payment, name='submit_payment'),
    path('confirm/', confirm, name='confirm'),
    path('paypal/', paypal, name='paypal'),
 

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
