from django.contrib import admin
from .models import Product, Category, AlertConfiguration, NotificationLog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'sku', 'batch_number', 'expiry_date', 'days_to_expiry', 'expiry_status']
    list_filter = ['category', 'unit', 'is_active']
    search_fields = ['product_name', 'sku', 'batch_number']
    ordering = ['expiry_date']


@admin.register(AlertConfiguration)
class AlertConfigAdmin(admin.ModelAdmin):
    list_display = ['threshold_days', 'alert_level', 'is_active']


@admin.register(NotificationLog)
class NotificationLogAdmin(admin.ModelAdmin):
    list_display = ['product', 'alert_level', 'recipient_email', 'date_sent', 'status']
    list_filter = ['status', 'alert_level']
