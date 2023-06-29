from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('lineiteem_total')


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date_now', 'order_total')

    fields = ('order_number', 'user_profile')

    list_display = ('full_name', 'date_now', 'order_number', 'order_total')


admin.site.register(Order, OrderAdmin)
