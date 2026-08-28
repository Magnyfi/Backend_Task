from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def home(request):

    context = {'Items' : Item.objects.all()}
    return render(request, 'store/home.html', context)



# Create your views here.
