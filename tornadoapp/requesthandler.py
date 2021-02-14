# Tornado Request handlers


import tornado.web

class Main(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World!")