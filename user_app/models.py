from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'profileImage', default= 'profileImage/no-profile.png', null=True)
    phone = models.CharField(max_length=14,blank=True,null=True)
    date_of_Birth = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.user.username
