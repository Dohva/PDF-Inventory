import os, shutil
from jinja2 import Template, Environment, FileSystemLoader
from config import Config

class SiteGenerator(object):
    def __init__(self, title, table):
        self.env = Environment(loader=FileSystemLoader('template'))
        self.title = title
        self.table = table
        folder = Config().publicDir
        self.empty_public(folder)
        self.copy_static(folder)
        self.render_page(folder)

    def empty_public(self, folder):
        """ Ensure the public directory is empty before generating. """
        try:
            shutil.rmtree(folder) 
            os.mkdir(folder)
        except FileNotFoundError:
            print("'public' folder not found")

    def copy_static(self, folder):
        """ Copy static assets to the public directory """
        #try:
        shutil.copytree('template/static', f'{folder}/static')
        #except FileNotFoundError:
        #    print("'template/static' folder not found")

    def render_page(self, folder):
        print("Rendering page to static file.")
        template = self.env.get_template('_layout.html')
        with open(f'{folder}/index.html', 'w+') as file:
            html = template.render(
                title = self.title,
                table = self.table
            )
            file.write(html)