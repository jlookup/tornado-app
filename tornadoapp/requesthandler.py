# Tornado Request Handlers


import tornado.web

class Main(tornado.web.RequestHandler):
    def get(self):
        self.render("./templates/index.html")