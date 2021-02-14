# Master list of app routes

import tornadoapp.requesthandler as rh


routes = [
    (r'/', rh.Main),
    (r'/api', rh.Api)
]