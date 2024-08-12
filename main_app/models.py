from django.db import models

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
