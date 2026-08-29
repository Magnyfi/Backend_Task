from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Wallet,Transactions
from django.contrib import messages
from django.db import transaction
from .forms import TopUpForm

@login_required
def wallet_home(request):
    user_wallet, created = Wallet.objects.get_or_create(user = request.user)

    if request.method == 'POST':
            form = TopUpForm(request.POST)
            if form.is_valid():
                amount = form.cleaned_data['amount']
    
                with transaction.atomic():
                    user_wallet.balance += amount
                    user_wallet.save()
                    
                    Transactions.objects.create(
                        wallet=user_wallet,
                        amount=amount,
                        status = True
                    )
                
                messages.success(request, f"Successfully added ${amount:.2f} to your wallet!")
                return redirect('wallet-home')
    else:
        form = TopUpForm()
    

    transactions = user_wallet.transactions.order_by('time')
    return render(request, 'wallet/walet-home.html', {'user_wallet':user_wallet, 'transactions':transactions, 'form': form})

'''
@login_required
def topup_wallet(request):
    user_wallet, created = Wallet.objects.get_or_create(user = request.user)
    if request.method == 'POST':
        form = TopUpForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']

            with transaction.atomic():
                user_wallet.balance += amount
                user_wallet.save()
                
                Transactions.objects.create(
                    wallet=user_wallet,
                    amount=amount,
                    status = True
                )
            
            messages.success(request, f"Successfully added ${amount:.2f} to your wallet!")
            return redirect('wallet-home')
    else:
        form = TopUpForm()

    return redirect('wallet-home')
'''
# Create your views here.
