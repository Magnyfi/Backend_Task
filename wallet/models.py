from django.db import models
from django.contrib.auth.models import User
from store.models import Item
from django.db.models.signals import post_save
from django.dispatch import receiver

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

    Last_Updated = models.DateTimeField(auto_now = True)
    

@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):

    if created:
        Wallet.objects.create(user=instance)

# Create your models here.
