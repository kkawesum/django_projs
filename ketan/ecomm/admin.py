from django.contrib import admin
from .models import Item,Order,OrderItem

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Item)
# Register your models here.
