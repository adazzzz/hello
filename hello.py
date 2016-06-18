# -*- coding:utf-8 -*-

import tornado.web
import tornado.ioloop

#Web framework
#tornado.web — RequestHandler and Application classes
#tornado.web.RequestHandler 是一个类
#tornado.web.Application 也是一个类

class Damu(tornado.web.RequestHandler):
	def get(self):
		self.write('hello world')
# get是这个handler的方法，get没有定义的。
# write也是一个方法method，这个handle已经定义过了。将括号内的内容(object)以class定义的method(方式)pass(传递)过去。

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
# [list]，{dictionary}
# 把class实例化成一个object
# r是一个字符串的修饰符，意思是后面是个路径？？？待确认
# 这段适合CV式coding，实际是一个ioloop包，里面再一个IOLoop包，把instance这个class实例化
# instance（）不传参数，它就是一直没有特点的猫。


if __name__=="__main__":
	main()

#这个也cv吧！调用主程序的惯用方法。