from rest_framework import filters, viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from cars.serializers import CarSerializer
from cars.models import Car
from rest_framework.response import Response


class CarModelViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Car.objects.all().order_by("-updated_at")
    filter_backends = [filters.SearchFilter]
    search_fields = ["id", "name", "brand"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
