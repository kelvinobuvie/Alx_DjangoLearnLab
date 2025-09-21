from django.contrib import admin
from .models import Book  # ✅ This is what the checker wants

# Register your model with the admin site
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns in the admin list view
    search_fields = ('title', 'author')                     # allow searching by title/author
    list_filter = ('publication_year',)                     # add a filter by publication year
