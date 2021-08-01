'''
Snippet #128-hello world webapp with tornado
stevepython.wordpress.com

Tested on Win 7.

source:
https://dev.to/petercour/python-web-programming-with-tornado-328n

pip 3install tornado
'''

import tornado.ioloop
import tornado.web

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello, world")

app = tornado.web.Application([ (r"/", HomeHandler), ])
app.listen(5000)
tornado.ioloop.IOLoop.instance().start()


# run only from terminal\dos box with yourprogram.py
# open webbrowser
# paste in: http://localhost:5000
# see hello frickin world
