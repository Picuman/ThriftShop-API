from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Item(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used_good', 'Used - Good'),
        ('used_fair', 'Used - Fair'),
    ]

    # The seller is the user who uploaded the item
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='used_good')
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.title