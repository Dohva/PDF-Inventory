from src.models.book import Book
from PyPDF2 import PdfFileReader
import pandas as pd
import os

def IsPDF(path):
    """Returns True if path's file is PDF, and False otherwise"""
    if path.endswith('.pdf'):
        return True
    else:
        return False

def IsValidTitle(title):
    if title is None:
        return False
    reject = ["", "none", "untitled"]
    if title.lower() in reject:
        return False
    else:
        return True

def GetBooksFromDir(path):
    """Recursively search through directories and return list of Book objects from PDF"""
    books = []
    for entry in os.listdir(path):
        item = os.path.join(path, entry)
        if os.path.isfile(item) and IsPDF(item):
            with open(item, 'rb') as f:
                pdf = PdfFileReader(f)
                book = Book(pdf, item)
                books.append(book)
        elif os.path.isdir(item):
            books.extend(GetBooksFromDir(item))
    return books

def DataFrameFromBooks(books):
    data = []
    for book in books:
       data.append(book.ToDict())
    return pd.DataFrame(data)
