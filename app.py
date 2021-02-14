'''
Tornado Web App
Jason Thomas
Copyright 2021
'''

# standard library

# third-party packages
import tornado.ioloop

# internal modules
from config import *
from tornadoapp import make_app 

if __name__ == '__main__':
    app = make_app()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
    print(f'[START] listening on {PORT}')