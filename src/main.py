import tkinter as tk
import pandas as pd
from book import Book
from config import Config
from helpers import *

def main():
    cf = Config()

    books = GetBooksFromDir(cf.basepath, cf.allowedExtensions)
    df = DataFrameFromBooks(books)

    # print(df.head())
    print(df.to_html())

if __name__ == "__main__":
    main()
