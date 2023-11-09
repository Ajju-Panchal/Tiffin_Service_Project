from django.contrib import admin
from .models import VendorProfile
# Register your models here.

class VendorProfileAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'vendor_mobile_number')

admin.site.register(VendorProfile, VendorProfileAdmin)

