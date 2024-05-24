from django.contrib import admin
from .models import Order, Contact

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display=('full_name', 'phone_number','address', 'cylinder_size','quantity','total_amount')


class ContactAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'message')

admin.site.register(Order, OrderAdmin)
admin.site.register(Contact, ContactAdmin)