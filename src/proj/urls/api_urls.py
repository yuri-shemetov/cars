from django.urls import path, include


app_name = "api"
urlpatterns = [
    path("auth/", include("authentication.urls", namespace="auth")),
    path("cars/", include("cars.urls", namespace="cars")),
]
