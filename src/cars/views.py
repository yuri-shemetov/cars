from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from cars.serializers import CarSerializer
from cars.models import Car


class CarModelViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Car.objects.all().order_by('-updated_at')
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name', 'brand']
