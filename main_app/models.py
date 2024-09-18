from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    subject = models.CharField(max_length=450)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'ContactInformation'
    def __str__(self):
        return self.name

#banner image
class Banner(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='banner_image/')
    product = models.CharField(max_length=400,null=True, blank=True)
    price = models.CharField(max_length=2)
    dis_price = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = ("Banner")
    def __str__(self):
        return self.name

#Product Category
class Category(models.Model):
    c_name = models.CharField(max_length=50, null=False)
    img = models.ImageField(upload_to = 'category_images/', null=False)
    details = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Category'
    
    def __str__(self):
        return self.c_name
    
#Brand name
class Brand(models.Model):
    name = models.CharField(max_length=50, null=False)
    img = models.ImageField(upload_to = 'category_images/', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Brands'
    
    def __str__(self):
        return self.name
    
#product
class Product(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='ProductImage')
    regular_price = models.PositiveIntegerField()
    discount_price = models.PositiveIntegerField(blank=True, null=True)
    discriptions = models.TextField()
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name

#Cart
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

#Wishlist
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username}'s wishlist - {self.product.name}"



#order
class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"order(self.product.name) - (self.quantity)"

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    delivery_area = models.CharField(max_length=20, choices=[('inside_dhaka', 'Inside Dhaka'), ('outside_dhaka', 'Outside Dhaka')])
    
    