from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
