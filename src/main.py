import tkinter as tk
import pandas as pd
from pandastable import Table
from book import Book
from config import Config
from helpers import *

def main():
    cf = Config()

    books = GetBooksFromDir(cf.basepath, cf.allowedExtensions)
    df = DataFrameFromBooks(books)

    print(df.head())

if __name__ == "__main__":
    main()
