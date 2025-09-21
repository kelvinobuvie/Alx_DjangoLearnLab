```python
# Retrieve the book you just created
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.title
book.author
book.publication_year
# Expected output (example):
# '1984'
# 'George Orwell'
# 1949
```
