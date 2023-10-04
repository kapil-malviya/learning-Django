from django.contrib import admin
from testapp.models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author', 'pages', 'price']