# -*- coding:utf-8 -*-

import tornado.web
import tornado.ioloop

#试图写一个计算器玩，木有可点击界面。你打我呀~~~
#分别写加减乘除四个class
#文本提示输入（输入格式懒得写，先省了吧）
#写结果输出
#GO!


#http://localhost:1234/calculator?a1=1&a2=2

class Mainpage(tornado.web.RequestHandler):
	def get(self):
		self.write("""
			<form action="/calculator" method="get">
				<p>First number: <input type="int" name="a1" /></p>
  				<p>Second number: <input type="int" name="a2" /></p>
  				<input type="submit" value="Submit" />
  			</form>
		""")


class Add(tornado.web.RequestHandler):
	def get(self, a, b):
		self.write( str(int(a) + int(b)) )

class Sub(tornado.web.RequestHandler):
	def get(self, a, b):
		self.write( str(int(a) - int(b)) )

class Mul(tornado.web.RequestHandler):
	def get(self, a, b):
		self.write( str(int(a) * int(b)) )

class Div(tornado.web.RequestHandler):
	def get(self, a, b):
		self.write( str(int(a) / int(b)) )

#class Calculator(tornado.web.RequestHandler):
#	def get(self, a1):
#		print a1
#		self.write( str(a1) )
	

def main():
	app = tornado.web.Application([
		(r"/",Mainpage),
		(r"/add/([0-9]+)/([0-9]+)",Add),
		(r"/sub/([0-9]+)/([0-9]+)",Sub),
		(r"/mul/([0-9]+)/([0-9]+)",Mul),
		(r"/div/([0-9]+)/([0-9]+)",Div)
#		(r"/calculator*",Calculator)
		])
	app.listen(1234)
	tornado.ioloop.IOLoop.instance().start()

if __name__=="__main__":
	main()