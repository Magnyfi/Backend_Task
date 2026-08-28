from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm
from .models import Item,CartItem,Cart
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request, f'Account created for {username}!Now login')
           return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' :form})

@login_required
def cart(request):
    user_cart_items = request.user.cart.items.all()
    return render(request, 'users/cart.html',{'cartitems': user_cart_items})

@login_required
def add_to_cart(request, item_id):

    item = get_object_or_404(Item, id=item_id)
    
    user_cart = request.user.cart
    #user_cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=user_cart,
        item=item
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()
        
    return redirect('store-cart')

@login_required
def sub_from_cart(request, item_id):

    item = get_object_or_404(Item, id=item_id)
    
    user_cart = request.user.cart
    #user_cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=user_cart,
        item=item
    )
    if created:
        cart_item.delete()
    else:
        cart_item.quantity -= 1
        if cart_item.quantity<1:
            cart_item.delete()
        else:
            cart_item.save()
        
    return redirect('store-cart')




# Create your views here.
