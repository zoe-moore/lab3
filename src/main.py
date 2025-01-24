import cherrypy
import os.path
import random
import datetime
import mako.template
import mako.lookup
import page_signup 

names = ["Michelangelo", "Donatello", "Raphael", "Leonardo"]
time_list = []
view_list = []

for i in range(10):
    x = datetime.timedelta(minutes=random.randrange(8000))
    hoursago = int( x.seconds / 3600 )
    minutesago = round((x.seconds % 3600)/60)
    if x.days!=1:
        time_list.append(f"{x.days} days, {hoursago} hours, and {minutesago} minutes ago")
    elif x.days==1:
        time_list.append(f"{x.days} day, {hoursago} hours, and {minutesago} minutes ago")

    view_list.append(random.randint(0,300))

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
        t = lookup.get_template("page_posts.html")
        return t.render(time_list = time_list, view_list = view_list)
        
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
