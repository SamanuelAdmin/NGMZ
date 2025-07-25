from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('tag', 'name', 'data')
    list_filter = ('tag', 'name')
    prepopulated_fields = {"tag": ("name",)}


@admin.register(CategoryGroup)
class CategoryGroupAdmin(admin.ModelAdmin):
    list_display = ('tag', 'name')
    list_filter = ('tag', 'name')
    prepopulated_fields = {"tag": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('tag', 'name')
    list_filter = ('tag', 'name')
    prepopulated_fields = {"tag": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('tag', 'name')
    list_filter = ('tag', 'name')
    prepopulated_fields = {"tag": ("name",)}