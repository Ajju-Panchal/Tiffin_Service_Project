from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class VendorProfile(models.Model):

    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor_mobile_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.vendor_first_name} {self.vendor_last_name}"
