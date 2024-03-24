from django.contrib import admin
from .models import Smoothie, Category

# Register your models here.

class SmoothieAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Smoothie, SmoothieAdmin)
admin.site.register(Category, CategoryAdmin)

