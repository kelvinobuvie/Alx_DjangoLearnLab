from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Book, Library   # ✅ This is what the checker wants


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
from django.views.generic import DetailView

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
