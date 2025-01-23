import cherrypy
import os.path
import random
import mako.template
import mako.lookup

names = ["Michelangelo", "Donatello", "Raphael", "Leonardo"]

images = ["..\\html\\logo.png","..\\html\\N2dS-Sc__400x400.jpg", "..\\html\\Untitled.png"]

#we have modules for each page we're displaying 
import page_index
import page_signup 
import page_posts

PYPATH= os.path.dirname(__file__)
lookup = mako.lookup.TemplateLookup(
    directories=[os.path.dirname(__file__)]
)


class App:
    @cherrypy.expose
    def index(self):
        n = random.choice(names)
        t = lookup.get_template("page_index.html")
        return t.render(name = n)
    @cherrypy.expose
    def signup(self):
        return page_signup.get()
    @cherrypy.expose
    def posts(self):
        i = random.choice(images)
        t = lookup.get_template("page_posts.html")
        return t.render(image = i)
        
#the location where the main.py file is stored: The src folder
srcdir = os.path.abspath(os.path.dirname(__file__))

app = App()
cherrypy.quickstart(
    app,
    '/',
    {
        "/html": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": f"{srcdir}/../html"
        }
    }
)
