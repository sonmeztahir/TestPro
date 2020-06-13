from django.contrib import admin
from .models import ThemeModel

class ThemeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publishing_date')

    class Meta:
        model = ThemeModel

admin.site.register(ThemeModel, ThemeModelAdmin)