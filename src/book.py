# src/book.py
import os
class Book():
    def __init__(self, path, basepath):
        if not isinstance(path, str):
            raise TypeError
        if not isinstance(basepath, str):
            raise TypeError
        self.path = path
        tags = os.path.split(path)[0]
        self.tags = tags.lstrip(basepath).split('\\')
        filename = os.path.split(path)[-1]
        split = os.path.splitext(filename)
        self.title = split[0]
        self.ext = split[1]
        print(self)
    def __str__(self):
        return f"{self.title}{self.tags}"
    def __repr__(self):
        return f"{self.title}{self.tags}"
    def ToDict(self):
        return {
            "title": self.title,
            "ext": self.ext,
            "tags": self.tags,
            "path": self.path
            }