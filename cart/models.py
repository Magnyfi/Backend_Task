from django.db import models
from django.contrib.auth.models import User
from store.models import Item
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

# Create your models here.
class Cart(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def total_price(self):
        
        return sum(item.total_price for item in self.items.all())


@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        
        return self.item.Price * self.quantity

    def clean(self):
        if self.item and self.quantity > self.item.Stock:
            raise ValidationError(
                f"Cannot add {self.quantity} units. Only {self.item.Stock} available in stock."
            )

    def save(self, *args, **kwargs):
        # Ensure full_clean() is run before saving to trigger clean()
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.item.Name}"

