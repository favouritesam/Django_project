from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'isbn', 'author']
    list_per_page = 10
    list_filter = ['title']
    search_fields = ['genre']


# add BookAdmin into admin.site.register
# admin.site.register(models.Book, BookAdmin)

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_filter = ['first_name', 'last_name']
    search_fields = ['email']
