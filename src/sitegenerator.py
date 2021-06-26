import os, shutil
from jinja2 import Template, Environment, FileSystemLoader

class SiteGenerator(object):
    def __init__(self, title, table):
        self.env = Environment(loader=FileSystemLoader('template'))
        self.title = title
        self.table = table
        self.empty_public()
        self.copy_static()
        self.render_page()

    def empty_public(self):
        """ Ensure the public directory is empty before generating. """
        try:
            shutil.rmtree('./public') 
            os.mkdir('./public')
        except FileNotFoundError:
            print("'public' folder not found")

    def copy_static(self):
        """ Copy static assets to the public directory """
        #try:
        shutil.copytree('template/static', 'public/static')
        #except FileNotFoundError:
        #    print("'template/static' folder not found")

    def render_page(self):
        print("Rendering page to static file.")
        template = self.env.get_template('_layout.html')
        with open('public/index.html', 'w+') as file:
            html = template.render(
                title = self.title,
                table = self.table
            )
            file.write(html)