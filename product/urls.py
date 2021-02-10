from rest_framework.routers import SimpleRouter

from product.views import ProductViewSet

router = SimpleRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = router.urls
