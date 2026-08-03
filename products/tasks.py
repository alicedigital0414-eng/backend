from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings


def check_expiry_alerts_sync():
    """Check expiry alerts and send notifications. Returns count of alerts sent."""
    from .models import Product, AlertConfiguration, NotificationLog
    from django.contrib.auth.models import User

    today = timezone.now().date()
    products = Product.objects.filter(is_active=True)
    alert_configs = AlertConfiguration.objects.filter(is_active=True).order_by('threshold_days')
    alert_recipients = User.objects.filter(
        is_active=True,
        profile__receive_email_alerts=True
    ).values_list('email', flat=True)
    alert_recipients = [e for e in alert_recipients if e]

    alerts_sent = 0

    for product in products:
        days_remaining = (product.expiry_date - today).days
        for config in alert_configs:
            if days_remaining <= config.threshold_days:
                # Check if we already sent this alert today
                already_sent = NotificationLog.objects.filter(
                    product=product,
                    alert_configuration=config,
                    date_sent__date=today
                ).exists()

                if not already_sent:
                    subject = f"[{config.alert_level}] Product Expiry Alert: {product.product_name}"
                    if days_remaining < 0:
                        body = f"EXPIRED: {product.product_name} (SKU: {product.sku}, Batch: {product.batch_number}) expired {abs(days_remaining)} day(s) ago on {product.expiry_date}. Quantity: {product.quantity} {product.unit}. Please remove from inventory immediately."
                    else:
                        body = f"Alert: {product.product_name} (SKU: {product.sku}, Batch: {product.batch_number}) expires in {days_remaining} day(s) on {product.expiry_date}. Quantity: {product.quantity} {product.unit}. Supplier: {product.supplier_name}. Please take appropriate action."

                    for email in alert_recipients:
                        log_status = 'PENDING'
                        try:
                            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)
                            log_status = 'SENT'
                            alerts_sent += 1
                        except Exception as e:
                            log_status = 'FAILED'

                        NotificationLog.objects.create(
                            product=product,
                            alert_configuration=config,
                            alert_level=config.alert_level,
                            recipient_email=email,
                            status=log_status,
                            message=body,
                            days_to_expiry_at_time=days_remaining
                        )

    return alerts_sent


# Celery task (used when Redis/Celery is available)
try:
    from celery import shared_task

    @shared_task
    def check_expiry_alerts():
        return check_expiry_alerts_sync()
except ImportError:
    pass
