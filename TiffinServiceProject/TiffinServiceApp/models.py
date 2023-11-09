from django.db import models
from vendorApp.models import VendorProfile
from userApp.models import user_or_service_address

# Create your models here.
class VendorTiffinService(models.Model):

    tiffin_service_vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    tiffin_service_name = models.CharField(max_length=100)
    tiffin_service_address = models.ForeignKey(user_or_service_address, on_delete=models.CASCADE)

    def __str__(self):
        return self.tiffin_service_name
