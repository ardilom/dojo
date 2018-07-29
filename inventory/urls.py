from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, IndexView

router = DefaultRouter()
router.register(r'products', ProductViewSet, base_name='product')

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index")
] + router.urls
