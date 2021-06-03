from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Product,Order,Cart,Category,Address
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from .forms import CartForm,SearchForm
from django.db.models import Sum
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            username = user.cleaned_data.get('username')
            messages.success(request,'Successfully Registered')
            return redirect('login')
        else:
            messages.error(request,'Failed to register')
            return render(request,'register.html',{'form':user})
    user = UserCreationForm()
    return render(request,'register.html',{'form':user})

@login_required
def cart(request):
    if request.method== 'POST':
        pass
    x = Cart.objects.filter(user_id=request.user.id)
    sum = x.aggregate(Sum('cost'))
    return render(request,'cart.html',{'x':x,'sum':sum})

@login_required
def remove(request,pk):
    instance=Cart.objects.get(order_id=pk)
    instance.delete()
    messages.success(request,'Removed from Cart')
    return redirect('cart')

@login_required
def homepage(request):
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request,'homepage.html',{'product':product,'category':category})

@login_required
def category(request,pk):
    cat = Category.objects.filter(category_id=pk)
    product = Product.objects.filter(category_id=pk)
    return render(request,'category.html',{'product':product,'category': cat})

@login_required
def product(request,pk):
    
    product = Product.objects.filter(product_id=pk)
    if request.method == 'POST':
        inst = Product.objects.get(product_id=pk)
        mess = CartForm(request.POST)
        if mess.is_valid():
            m = mess.save(commit=False)
            m.user_id = request.user
            m.prodect_id = inst
            # m.cost = float("{:.2f}".format(inst.price * mess.cleaned_data.get("quantity")))
            m.cost = float("{:.2f}".format(inst.price*mess.cleaned_data.get("quantity")))
            print(m.cost)
            m.save()
            messages.success(request,'Product added to Cart')
        else:
            messages.error(request,'Failed to add')
    form = CartForm(initial={'quantity':1})
    return render(request,'product.html',{'product':product,'form':form})


@login_required
def buy(request,pk):
    orders = Cart.objects.filter(user_id=pk)
    for x in orders:
        s = Order()
        s.user_id = request.user
        s.product_id = x.prodect_id
        s.quantity = x.quantity
        s.cost = x.cost
        s.time = timezone.now()
        s.save()
        x.delete()
    messages.success(request,'Your order is on the way! Happy shopping')
    print(orders)
    return redirect('cart')

@login_required
def my_orders(request):
    orders = Order.objects.filter(user_id=request.user.id)
    orders = orders.order_by('time')
    return render(request,'order.html',{'orders':orders})

@login_required
def cancel_order(request,pk):
    orders = Order.objects.get(order_id=pk)
    orders.delete()
    messages.success(request,'Order Cancelled')
    return redirect('orders')

@login_required
def search(request):
    if request.method=="POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            search_result = Product.objects.filter(name__icontains=username)
            if search_result == None:
                messages.error(request,'No product found')
            return render(request,'search.html',{'search_result':search_result,'form':form})
    else:
        form = SearchForm()
        return render(request,'search.html',{'form':form})

@login_required
def search_from_any_page(request):
    search_text = request.POST.get('search_text',None)
    if search_text == None:
        messages.error(request,'No product found')
        return redirect('search')
    else:
        form = SearchForm()
        search_result = Product.objects.filter(name__icontains=search_text)
        return render(request,'search.html',{'search_result':search_result,'form':form})