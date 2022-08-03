from cars.views import CarModelViewSet

from rest_framework.routers import DefaultRouter


app_name = 'cars'
# Create router and Registration ViewSet
router = DefaultRouter()
router.register(r'', CarModelViewSet, basename='cars')
# URLs
urlpatterns = router.urls
