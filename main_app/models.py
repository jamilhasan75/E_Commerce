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
