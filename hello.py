import tornado.web
import tornado.ioloop

class Damu(tornado.web.RequestHandler):
	def get(self):
		self.write('hello world')

class SmallDamu(tornado.web.RequestHandler):
	"""docstring for ClassName"""
	def get(self):
		self.write('hi world')
		


# for i in range(2,10):
	# print i


def main():
	app = tornado.web.Application([
		(r"/",Damu),
		(r"/s",SmallDamu)])
	app.listen(1234)
	tornado.ioloop.IOLoop.instance().start()

if __name__=="__main__":
	main()