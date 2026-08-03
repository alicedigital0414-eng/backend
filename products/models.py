from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    UNIT_CHOICES = [
        ('pieces', 'Pieces'),
        ('kg', 'Kilograms'),
        ('g', 'Grams'),
        ('litres', 'Litres'),
        ('ml', 'Millilitres'),
        ('packs', 'Packs'),
        ('boxes', 'Boxes'),
        ('bottles', 'Bottles'),
        ('tablets', 'Tablets'),
        ('capsules', 'Capsules'),
    ]

    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    sku = models.CharField(max_length=100, unique=True, verbose_name='SKU')
    batch_number = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, default='pieces')
    manufacture_date = models.DateField()
    expiry_date = models.DateField()
    supplier_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='products')
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['expiry_date']

    def __str__(self):
        return f"{self.product_name} ({self.batch_number})"

    @property
    def days_to_expiry(self):
        today = timezone.now().date()
        delta = self.expiry_date - today
        return delta.days

    @property
    def expiry_status(self):
        days = self.days_to_expiry
        if days < 0:
            return 'expired'
        elif days <= 7:
            return 'critical'
        elif days <= 14:
            return 'warning'
        elif days <= 30:
            return 'near_expiry'
        else:
            return 'safe'

    @property
    def expiry_status_display(self):
        mapping = {
            'expired': 'Expired',
            'critical': 'Critical (≤7 days)',
            'warning': 'Warning (≤14 days)',
            'near_expiry': 'Near Expiry (≤30 days)',
            'safe': 'Safe',
        }
        return mapping.get(self.expiry_status, 'Unknown')


class AlertConfiguration(models.Model):
    LEVEL_CHOICES = [
        ('INFO', 'Info'),
        ('WARNING', 'Warning'),
        ('CRITICAL', 'Critical'),
    ]

    threshold_days = models.PositiveIntegerField(help_text='Days before expiry to trigger alert')
    alert_level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='INFO')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['threshold_days']

    def __str__(self):
        return f"{self.alert_level} alert at {self.threshold_days} days"


class NotificationLog(models.Model):
    STATUS_CHOICES = [
        ('SENT', 'Sent'),
        ('FAILED', 'Failed'),
        ('PENDING', 'Pending'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='notifications')
    alert_configuration = models.ForeignKey(AlertConfiguration, on_delete=models.SET_NULL, null=True)
    alert_level = models.CharField(max_length=10)
    recipient_email = models.EmailField()
    date_sent = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    message = models.TextField(blank=True)
    days_to_expiry_at_time = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date_sent']

    def __str__(self):
        return f"Alert for {self.product} to {self.recipient_email} - {self.status}"
