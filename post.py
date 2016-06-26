# -*- coding:utf-8 -*-

import tornado.web
import tornado.ioloop

#试图写一个post工具，可以发布、查看列表及详情。

#get + post
#存储为文件
#读取文件
#输出文件列表

class MyFormHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/myform" method="POST">'
                   '<input type="title" name="title">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

class FileHandler(tornado.web.RequestHandler):
    def get(self, filename):
        self.set_header("Content-Type", "text/plain")
        with open(filename) as sample:
            self.write(sample.read())

    def post(self, filename):
        self.set_header("Content-Type", "text/plain")
        with open(filename, 'w') as sample:
            sample.write(self.get_body_argument("title") + self.get_body_argument("message"))
            self.write('ok')

class ListHandler(tornado.web.RequestHandler):
    def get(self):
        from os import listdir
        self.write('\n'.join(listdir('.')))
#以下均为套路

def main():
    app = tornado.web.Application([
        (r"/",MyFormHandler),
        (r"/myform",FileHandler),
#        (r"/myform/([0-9]+)",FileHandler),
        (r"/list",ListHandler)
        ])
    app.listen(1234)
    tornado.ioloop.IOLoop.instance().start()

if __name__=="__main__":
    main()