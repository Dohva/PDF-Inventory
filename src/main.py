from src.models import Book
from src.inventory import *
import pandas as pd

basepath = r"C:\Users\Rasmus\Google Drive\D&D 5E\books"

books = GetBooksFromDir(basepath)
df = DataFrameFromBooks(books)
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df)