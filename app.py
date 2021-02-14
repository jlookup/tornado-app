'''
Tornado Web App
Jason Thomas
Copyright 2021
'''

# standard library

# third-party packages
import tornado.ioloop
import tornado.web

# internal modules
from config import *
import tornadoapp.requesthandler as rh
from tornadoapp.routes import routes

def make_app():
    return tornado.web.Application(routes)

if __name__ == '__main__':
    app = make_app()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
    print(f'[START] listening on {PORT}')