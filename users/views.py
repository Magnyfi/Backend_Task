from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm
from cart.models import Item,CartItem,Cart
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



# Create your views here.
