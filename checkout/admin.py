from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date')
    inlines = (OrderLineItemAdminInLine,)

    fields = ('order_number', 'date', 'full_name', 'email',
              'phone_number', 'postcode', 'country', 'county',
              'town_or_city', 'street_address1', 'street_address2',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)

