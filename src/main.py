# src/main.py
from sitegenerator import SiteGenerator as Page
from book import Book
from config import Config
from helpers import *

def main():
    cf = Config()

    books = GetBooksFromDir(cf.basepath, cf.allowedExtensions)
    df = DataFrameFromBooks(books)

    table = df.to_html()
    Page("PDF-Inventory", table)

if __name__ == "__main__":
    main()
