import uuid
from django.db import models


class Brand(models.TextChoices):
    BMW = 'BMW'
    AUDI = 'Audi'
    MERCEDES = 'Mercedes'


class Car(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    owner = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='cars'
    )
    name = models.CharField(
        max_length=80
    )
    brand = models.CharField(
        max_length=8,
        choices=Brand.choices,
        default=Brand.BMW,
    )
    photo = models.FileField(
        max_length=30,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
    )
