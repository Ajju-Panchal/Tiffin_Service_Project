from django.contrib import admin
from .models import VendorTiffinService

# Register your models here.
class VendorTiffinServiceAdmin(admin.ModelAdmin):
    list_display = ('tiffin_service_name', 'tiffin_service_vendor', 'tiffin_service_address')

admin.site.register(VendorTiffinService, VendorTiffinServiceAdmin)
