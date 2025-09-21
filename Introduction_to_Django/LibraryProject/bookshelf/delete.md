```python
# Delete the book you created
from bookshelf.models import Book   # ✅ This line is required

book = Book.objects.get(id=1)       # Get the book instance
book.delete()                       # Delete the book

# Confirm deletion
Book.objects.all()
# Expected output: <QuerySet []>  (an empty queryset after deletion)
```
