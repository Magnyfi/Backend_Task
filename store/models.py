from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):

    Name = models.CharField(max_length=100)

    Description = models.TextField()

    Stock = models.PositiveIntegerField()

    Price = models.DecimalField(max_digits=10, decimal_places=2)

    Last_Updated = models.DateTimeField(auto_now = True)

    class Category(models.TextChoices):
        ELECTRONICS = 'ELECTRONICS', 'Electronics'
        GROCERY = 'GROCERY', 'Grocery'
        CLOTHING = 'CLOTHING', 'Clothing'
        HOME = 'HOME', 'Home & Kitchen'

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.GROCERY
    )

    class Unit(models.TextChoices):
        PIECE = 'PCS', 'Pieces (pcs)'
        KILOGRAM = 'KG', 'Kilogram (kg)'
        PACK = 'PACK', 'Pack'
        LITER = 'LITRE', 'Litre (L)'

    unit = models.CharField(
        max_length=10,
        choices=Unit.choices,
        default = Unit.PIECE
    )

    def __str__(self):
        return self.Name

