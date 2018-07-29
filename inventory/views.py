from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.views.generic.base import TemplateView

class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class IndexView(TemplateView):

    template_name = "inventory/index.html"

    # may be needed later
    def get_context_data(self, **kwargs):
        pass
