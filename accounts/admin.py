from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('sinif', 'numara',)}),)
    list_filter = ('numara',)
    list_display = ('username', 'first_name', 'last_name', 'sinif', 'numara')


admin.site.register(CustomUser, CustomUserAdmin)
