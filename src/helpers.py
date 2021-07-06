#src/helpers.py
from book import Book
import pandas as pd
import os

def GetBooksFromDir(path, exts, prefixPath = None):
    """Recursively search through directories and return list of Book objects from PDF"""
    books = []
    if prefixPath is None:
        prefixPath = path
    for entry in os.listdir(path):
        item = os.path.join(path, entry)
        if os.path.isfile(item):
            ext = os.path.splitext(item)[1]
            if ext in exts:
                book = Book(item, prefixPath)
                books.append(book)
        elif os.path.isdir(item):
            books.extend(GetBooksFromDir(item, exts, prefixPath))
    return books

def DataFrameFromBooks(books):
    data = []
    for book in books:
       data.append(book.ToDict())
    return pd.DataFrame(data)