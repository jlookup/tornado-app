# standard library

# third-party packages
import tornado.web

# internal modules
from tornadoapp.routes import routes

def make_app():
    return tornado.web.Application(routes)

