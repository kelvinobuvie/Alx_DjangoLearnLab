from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """Form for creating and updating Book instances."""
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author'}),
            'publication_year': forms.NumberInput(attrs={'min': 0}),
        }

    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        if year is not None and year < 0:
            raise forms.ValidationError("Publication year cannot be negative.")
        return year


class BookSearchForm(forms.Form):
    """Simple search form (optional)."""
    query = forms.CharField(required=False, label='Search', widget=forms.TextInput(attrs={'placeholder': 'Search by title or author'}))
