from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, permission_required, login_required
from django.http import HttpResponseForbidden
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# ====================================================
# ROLE-BASED ACCESS CONTROL VIEWS
# ====================================================

# helper checks
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    """View accessible only to Admin role."""
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    """View accessible only to Librarian role."""
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    """View accessible only to Member role."""
    return render(request, 'relationship_app/member_view.html')


# ====================================================
# BOOK CRUD VIEWS WITH PERMISSIONS
# ====================================================

@permission_required('relationship_app.can_add_book')
def add_book(request):
    """Add a new book (only users with can_add_book permission)."""
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        if title and author_id:
            # minimal example — you’d normally use a form
            from .models import Author
            author = get_object_or_404(Author, pk=author_id)
            Book.objects.create(title=title, author=author)
            return redirect('list_books')
    return render(request, 'relationship_app/add_book.html')


@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    """Edit an existing book (only users with can_change_book permission)."""
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title', book.title)
        book.save()
        return redirect('list_books')
    return render(request, 'relationship_app/edit_book.html', {'book': book})


@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    """Delete a book (only users with can_delete_book permission)."""
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})


# ====================================================
# BASIC VIEWS TO DISPLAY DATA (from earlier task)
# ====================================================

@login_required
def list_books(request):
    """Function-based view listing all books."""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


from django.views.generic.detail import DetailView

class LibraryDetailView(DetailView):
    """Class-based view showing a library’s details."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
