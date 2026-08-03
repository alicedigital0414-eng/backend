from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, AlertConfigurationViewSet, NotificationLogViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('categories', CategoryViewSet, basename='category')
router.register('alert-configs', AlertConfigurationViewSet, basename='alertconfig')
router.register('notifications', NotificationLogViewSet, basename='notification')

urlpatterns = router.urls
