from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # ✅ URL for function-based view listing books
    path('books/', list_books, name='list_books'),
    # ✅ URL for class-based view library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
