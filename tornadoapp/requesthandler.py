# Tornado Request Handlers


import tornado.web

handler = tornado.web.RequestHandler

class Main(handler):
    def get(self):
        self.render("./templates/index.html")

class Api(handler):
    '''API Endpoint. Takes the argument, 
    processes the request, and returns a response'''
    def get(self):
        n_str = self.get_argument("n")
        evenodd = self.is_even(n_str)
        self.write(f'The number {n_str} is {evenodd}.')

    def is_even(self, n: str) -> str:
        '''Takes a string or int n 
        returns string 'even' or 'odd'.'''
        n = int(str(n[-1]))
        return 'odd' if n % 2 else 'even'   

class Resource(handler):
    '''Handles a resource variable in the URL string'''
    def get(self, id: str):
        self.write(f'Getting blog post {id}.')