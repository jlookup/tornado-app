# Master list of app routes

import tornadoapp.requesthandler as rh


routes = [
    (r'/', rh.Main),
    (r'/api', rh.Api),
    (r'/resource/([0-9]+)', rh.Resource)
]