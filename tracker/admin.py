from django.contrib import admin
from .models import Condition, Device, Transaction

@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ('grade_name', 'price_modifier')
    search_fields = ('grade_name',)

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'base_market_price', 'condition')
    list_filter = ('brand', 'condition')
    search_fields = ('name', 'brand')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('device', 'transaction_type', 'actual_price', 'date')
    list_filter = ('transaction_type', 'date')