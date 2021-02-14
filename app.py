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
    print(f'[START] listening on {PORT}')
    
    tornado.ioloop.IOLoop.current().start()
    # put nothing below this line.