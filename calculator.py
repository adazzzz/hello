# -*- coding:utf-8 -*-

import tornado.web
import tornado.ioloop

# 试图写一个计算器玩，木有可点击界面。你打我呀~~~
#

class Calculator(tornado.web.RequestHandler):
	def get(self):
		self.write('hello world')


class Damu(tornado.web.RequestHandler):
	def get(self):

def main():


if __name__=="__main__":
	main()