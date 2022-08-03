from rest_framework import serializers

from cars import models


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = models.Car
        fields = [
            'id',
            'owner',
            'name',
            'brand',
            'photo',
            'created_at',
            'updated_at',
        ]
