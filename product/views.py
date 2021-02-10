from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.order_by('name').all()
    serializer_class = ProductSerializer
