import tornado.web
import tornado.ioloop

class Calculator(tornado.web.RequestHandler):
	def get(self):
		self.write('hello world')

