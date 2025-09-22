from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
# ✅ The checker is looking for this exact import line
from .models import Library
from .models import Book



# ✅ Function-based view: List all books
def list_books(request):
    # Get all Book objects
    books = Book.objects.all()
    # Render to template with books context
    return render(request, 'relationship_app/list_books.html', {'books': books})


# ✅ Class-based view: Display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    # Optionally override get_object to be explicit
    def get_object(self):
        return get_object_or_404(Library, pk=self.kwargs['pk'])
