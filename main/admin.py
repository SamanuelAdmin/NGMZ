from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


# Register your models here.
@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('tag', 'name', 'data')
    list_filter = ('tag', 'name')
    prepopulated_fields = {"tag": ("name",)}



@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('tag', 'name')
    list_filter = ('tag', 'name')
    search_fields = ('name_uk', "name_en")
    prepopulated_fields = {"tag": ("name_uk",)}


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('tag', 'name')
    list_filter = ('tag', 'name')
    search_fields = ('name_uk', "name_en")
    prepopulated_fields = {"tag": ("name_uk",)}