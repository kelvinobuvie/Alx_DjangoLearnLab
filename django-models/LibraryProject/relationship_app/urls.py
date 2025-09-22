from django.urls import path
from . import views
from .views import LibraryDetailView

urlpatterns = [
    # Function-based view for books
    path('books/', views.list_books, name='list_books'),

    # Class-based view for library detail
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # ==========================
    # ROLE BASED ACCESS URLS
    # ==========================
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # ==========================
    # PERMISSION-SECURED BOOK URLS
    # ==========================
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]
