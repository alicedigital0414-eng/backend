from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from django.db.models import Q
from django.http import HttpResponse
import csv

from .models import Product, Category, AlertConfiguration, NotificationLog
from .serializers import (
    ProductSerializer, CategorySerializer,
    AlertConfigurationSerializer, NotificationLogSerializer,
    DashboardSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True).select_related('category', 'added_by')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'unit']
    search_fields = ['product_name', 'sku', 'batch_number', 'supplier_name']
    ordering_fields = ['expiry_date', 'product_name', 'date_added', 'quantity']
    ordering = ['expiry_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        status_filter = self.request.query_params.get('expiry_status')
        if status_filter:
            today = timezone.now().date()
            if status_filter == 'expired':
                queryset = queryset.filter(expiry_date__lt=today)
            elif status_filter == 'critical':
                queryset = queryset.filter(expiry_date__gte=today, expiry_date__lte=today + timezone.timedelta(days=7))
            elif status_filter == 'warning':
                queryset = queryset.filter(expiry_date__gt=today + timezone.timedelta(days=7), expiry_date__lte=today + timezone.timedelta(days=14))
            elif status_filter == 'near_expiry':
                queryset = queryset.filter(expiry_date__gt=today + timezone.timedelta(days=14), expiry_date__lte=today + timezone.timedelta(days=30))
            elif status_filter == 'safe':
                queryset = queryset.filter(expiry_date__gt=today + timezone.timedelta(days=30))
        return queryset

    @action(detail=False, methods=['get'])
    def dashboard(self, request):
        today = timezone.now().date()
        products = Product.objects.filter(is_active=True)
        total = products.count()
        expired = products.filter(expiry_date__lt=today).count()
        critical = products.filter(expiry_date__gte=today, expiry_date__lte=today + timezone.timedelta(days=7)).count()
        warning = products.filter(expiry_date__gt=today + timezone.timedelta(days=7), expiry_date__lte=today + timezone.timedelta(days=14)).count()
        near_expiry = products.filter(expiry_date__gt=today + timezone.timedelta(days=14), expiry_date__lte=today + timezone.timedelta(days=30)).count()
        safe = products.filter(expiry_date__gt=today + timezone.timedelta(days=30)).count()
        expiring_today = products.filter(expiry_date=today).count()
        expiring_week = products.filter(expiry_date__gte=today, expiry_date__lte=today + timezone.timedelta(days=7)).count()
        expiring_month = products.filter(expiry_date__gte=today, expiry_date__lte=today + timezone.timedelta(days=30)).count()

        data = {
            'total_products': total,
            'expired_count': expired,
            'critical_count': critical,
            'warning_count': warning,
            'near_expiry_count': near_expiry,
            'safe_count': safe,
            'expiring_today': expiring_today,
            'expiring_this_week': expiring_week,
            'expiring_this_month': expiring_month,
        }
        return Response(data)

    @action(detail=False, methods=['get'])
    def analytics(self, request):
        today = timezone.now().date()
        products = Product.objects.filter(is_active=True)
        daily = []
        for i in range(7):
            day = today + timezone.timedelta(days=i)
            count = products.filter(expiry_date=day).count()
            daily.append({'date': str(day), 'count': count})
        weekly = []
        for i in range(4):
            week_start = today + timezone.timedelta(weeks=i)
            week_end = week_start + timezone.timedelta(days=6)
            count = products.filter(expiry_date__gte=week_start, expiry_date__lte=week_end).count()
            weekly.append({'week': f'Week {i+1}', 'start': str(week_start), 'end': str(week_end), 'count': count})
        monthly = []
        for i in range(3):
            month_start = today + timezone.timedelta(days=i*30)
            month_end = month_start + timezone.timedelta(days=29)
            count = products.filter(expiry_date__gte=month_start, expiry_date__lte=month_end).count()
            monthly.append({'label': f'Month {i+1}', 'count': count})
        return Response({'daily': daily, 'weekly': weekly, 'monthly': monthly})

    @action(detail=False, methods=['get'])
    def export_csv(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products_expiry_report.csv"'
        writer = csv.writer(response)
        writer.writerow(['Product Name', 'Category', 'SKU', 'Batch No.', 'Quantity', 'Unit',
                         'Manufacture Date', 'Expiry Date', 'Days To Expiry', 'Status', 'Supplier'])
        for p in self.get_queryset():
            writer.writerow([
                p.product_name, p.category.name if p.category else '',
                p.sku, p.batch_number, p.quantity, p.unit,
                p.manufacture_date, p.expiry_date, p.days_to_expiry,
                p.expiry_status_display, p.supplier_name
            ])
        return response

    @action(detail=False, methods=['post'])
    def trigger_alerts(self, request):
        from .tasks import check_expiry_alerts_sync
        result = check_expiry_alerts_sync()
        return Response({'message': 'Alert check complete', 'alerts_sent': result})


class AlertConfigurationViewSet(viewsets.ModelViewSet):
    queryset = AlertConfiguration.objects.all()
    serializer_class = AlertConfigurationSerializer
    permission_classes = [IsAuthenticated]


class NotificationLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NotificationLog.objects.all().select_related('product')
    serializer_class = NotificationLogSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'alert_level']
    ordering = ['-date_sent']
