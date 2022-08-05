from django.contrib import admin
from cars.models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ["id", "owner", "name", "brand"]


admin.site.register(Car, CarAdmin)
