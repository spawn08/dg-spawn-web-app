from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from flask_index import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(4789, 'localhost')
IOLoop.instance().start()
