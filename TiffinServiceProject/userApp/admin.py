from django.contrib import admin
from .models import user_or_service_address, UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile_number', 'gender', 'user_address')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_type', 'country', 'province', 'city', 'postal_code', 'address')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(user_or_service_address, AddressAdmin)
