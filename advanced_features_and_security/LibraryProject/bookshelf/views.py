from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .forms import BookForm
from .models import Book
from .forms import ExampleForm


# add_book view using BookForm
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_list.html', {'form': form})

# edit_book view using BookForm
@permission_required('bookshelf.form_example', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES or None, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form, 'book': book})

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # handle the form data
            # cleaned_data = form.cleaned_data
            return render(request, 'bookshelf/form_example.html', {'form': form, 'submitted': True})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})