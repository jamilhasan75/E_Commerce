from django.db import models
from django.utils import timezone

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
        return self.name
    
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