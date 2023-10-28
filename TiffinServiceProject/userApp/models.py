from django.db import models
from django.contrib.auth.models import User

# Create your models here.

    
class user_or_service_address(models.Model):

    # address_type = models.CharField(
    #     max_length=20,
    #     choices=[('vendor_address', 'Vendor Address'), ('user_address', 'User Address')],
    # )
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"{self.address_type} - {self.country}, {self.city}"
    
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_address = models.ForeignKey(user_or_service_address, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"