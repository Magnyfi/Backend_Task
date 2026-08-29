from django.db import models
from django.contrib.auth.models import User
from store.models import Item
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.validators import MinValueValidator
from decimal import Decimal

class Wallet(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    balance = models.DecimalField(max_digits=10, decimal_places=2,default = 0)

    class Currency(models.TextChoices):
            RUPEE = '₹','Rs'
            DOLLAR = '$', 'USD'
            POUND = '£', 'GBP'
            EURO = '€', 'EUR'
    
    currency = models.CharField(
            max_length=20,
            choices=Currency.choices,
            default=Currency.RUPEE
        )

    Last_Updated = models.DateTimeField(default = timezone.now)
    

@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):

    if created:
        Wallet.objects.create(user=instance)

class Transactions(models.Model):

     wallet = models.ForeignKey(Wallet,on_delete=models.SET_NULL, null=True, related_name='transactions',validators=[MinValueValidator(Decimal('0.00'))])
     amount = models.DecimalField(max_digits=10,decimal_places=2)
     time = models.DateTimeField(default = timezone.now)
     status = models.BooleanField(default = False)

     

# Create your models here.
