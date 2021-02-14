# Tornado Request Handlers


import tornado.web

handler = tornado.web.RequestHandler

class Main(handler):
    def get(self):
        self.render("./templates/index.html")

class Api(handler):
    def get(self):
        n = int(self.get_argument("n"))
        result = 'odd' if n % 2 else 'even'
        self.write(f'The number {str(n)} is {result}.')
        