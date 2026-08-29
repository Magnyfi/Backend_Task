from django.shortcuts import render, redirect, get_object_or_404
from .models import Item,CartItem,Cart
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def cart(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    user_cart_items = request.user.cart.items.all()
    return render(request, 'cart/cart.html',{'cartitems': user_cart_items,'cart':user_cart})

@login_required
def add_to_cart(request, item_id):

    item = get_object_or_404(Item, id=item_id)
    
    #user_cart = request.user.cart
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=user_cart,
        item=item
    )

    if not created:
        if (cart_item.quantity + 1)<=cart_item.item.Stock:
            cart_item.quantity += 1
        
        else:
            messages.error(request, f"Items cannot exceed item stock({cart_item.item.Stock}) ")

        cart_item.save()

    return redirect('store-cart')
    

@login_required
def sub_from_cart(request, item_id):

    item = get_object_or_404(Item, id=item_id)
    
    #user_cart = request.user.cart
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    
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
