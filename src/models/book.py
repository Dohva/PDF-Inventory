from src.inventory import IsValidTitle
from PyPDF2 import PdfFileReader
import os
class Book():
    def __init__(self, pdf, path):
        if not isinstance(pdf, PdfFileReader):
            raise TypeError
        if not isinstance(path, str):
            raise TypeError
        self.pdf = pdf
        self.path = path
        self.pages = pdf.getNumPages()
        info = pdf.getDocumentInfo()
        if info and info is not None and IsValidTitle(info.title):
            self.title = info.title
            self.author = info.author
            self.subject = info.subject
        else:
            filename = os.path.split(path)[-1]
            self.title = os.path.splitext(filename)[0]
            self.author = "..."
            self.subject = "..."
    def __str__(self):
        return f"{self.title}({self.pages} pages)"
    def ToDict(self):
        return {
            "title": self.title,
            "path": self.path,
            "pages": self.pages,
            "author": self.author,
            "subject": self.subject
        }