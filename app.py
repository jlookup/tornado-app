'''
Tornado Web App
2021 Jason Thomas
'''

# standard library

# third-party packages
import tornado.ioloop

# internal modules
from config import PORT
from tornadoapp import make_app 

if __name__ == '__main__':
    app = make_app()
    app.listen(PORT)
    print(f'[START] listening on {PORT}')

    # event loop starts below. Nothing after this will run
    tornado.ioloop.IOLoop.current().start()
    # nothing below this line