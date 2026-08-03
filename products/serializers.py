from rest_framework import serializers
from .models import Product, Category, AlertConfiguration, NotificationLog
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count', 'created_at']

    def get_product_count(self, obj):
        return obj.products.filter(is_active=True).count()


class ProductSerializer(serializers.ModelSerializer):
    days_to_expiry = serializers.ReadOnlyField()
    expiry_status = serializers.ReadOnlyField()
    expiry_status_display = serializers.ReadOnlyField()
    category_name = serializers.SerializerMethodField()
    added_by_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'product_name', 'category', 'category_name', 'sku',
            'batch_number', 'quantity', 'unit', 'manufacture_date',
            'expiry_date', 'supplier_name', 'description', 'date_added',
            'last_updated', 'added_by', 'added_by_name', 'is_active',
            'days_to_expiry', 'expiry_status', 'expiry_status_display',
        ]
        read_only_fields = ['date_added', 'last_updated', 'added_by']

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None

    def get_added_by_name(self, obj):
        if obj.added_by:
            return f"{obj.added_by.first_name} {obj.added_by.last_name}".strip() or obj.added_by.username
        return None

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['added_by'] = request.user
        return super().create(validated_data)


class AlertConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertConfiguration
        fields = ['id', 'threshold_days', 'alert_level', 'is_active', 'created_at']


class NotificationLogSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()

    class Meta:
        model = NotificationLog
        fields = [
            'id', 'product', 'product_name', 'alert_level',
            'recipient_email', 'date_sent', 'status',
            'message', 'days_to_expiry_at_time',
        ]

    def get_product_name(self, obj):
        return obj.product.product_name if obj.product else None


class DashboardSerializer(serializers.Serializer):
    total_products = serializers.IntegerField()
    expired_count = serializers.IntegerField()
    critical_count = serializers.IntegerField()
    warning_count = serializers.IntegerField()
    near_expiry_count = serializers.IntegerField()
    safe_count = serializers.IntegerField()
    expiring_today = serializers.IntegerField()
    expiring_this_week = serializers.IntegerField()
    expiring_this_month = serializers.IntegerField()
