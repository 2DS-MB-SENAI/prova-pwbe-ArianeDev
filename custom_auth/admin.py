from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'address', 'birth_date', 'is_verified')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'address', 'birth_date', 'is_verified')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'address', 'birth_date', 'is_verified')}),
    )

admin.site.register(CustomUser, UsuarioAdmin)
