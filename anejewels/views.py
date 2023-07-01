from django.shortcuts import render, redirect
from .models import Category, Product, Order, OrderProduct
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import ProductForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def home(request):
    categories = Category.objects.all()
    products = []

    for category in categories:
        category_products = list(Product.objects.filter(category=category)[:1])
        if category_products:
            products.append(category_products[0])

    context = {
        'categories': categories,
        'products': products,
    }

    return render(request, 'home.html', context)


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def product_list(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        'category': category,
        'products': products,
        'categories': categories,  
    }
    return render(request, 'product_list.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    categories = Category.objects.all()  
    context = {
        'product': product,
        'categories': categories,  
    }

    return render(request, 'product_detail.html', context)


def cart(request):
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)
    categories = Category.objects.all()
    cart_items = []
    total = 0
    for product in products:
        quantity = int(cart[str(product.id)]) 
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})

    context = {
        'cart_items': cart_items,
        'categories': categories,
        'total': total
    }

    return render(request, 'cart.html', context)


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    quantity = cart.get(str(product_id), 0)
    cart[str(product_id)] = quantity + 1
    request.session['cart'] = cart
    return redirect('cart')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
        messages.success(request, 'Product removed from cart.')
    return redirect('cart')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def add_product(request):
    if not request.user.is_staff:
        return redirect('home')  

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')


def payment(request):
 
    return render(request, 'payment.html')


def confirm(request):
    return render(request, 'confirm.html')


def paypal(request):
    return render(request, 'paypal.html')


def submit_payment(request):
    if request.method == 'POST':

        bank = request.POST.get('bank')
        account = request.POST.get('account')
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        order_product = OrderProduct(bank=bank, account=account, name=name, address=address, email=email, phone=phone)
        order_product.save()

        return redirect('confirm')  

    return redirect('payment') 
