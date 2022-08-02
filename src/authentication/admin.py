from django.contrib import admin
from authentication.models import User


class AuthenticationAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'token', ]


admin.site.register(User, AuthenticationAdmin)
