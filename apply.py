# -*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop
import os

#做一个input输入文本。姓名+手机号+备注 done
#提交后保存为一个表格。
#表格文件存在一个目录里 done

class ApplyFormHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/apply" method="POST">'
                   '<input type="text" name="name" value="name">'
                   '<input type="number" name="cellphone" value="138">'
                   '<input type="paragraph" name="reason" value="?">'
                   '<input type="submit" value="提交">'
                   '</form></body></html>')



class FileHandler(tornado.web.RequestHandler):
   # def get(self, filename):
   #     self.set_header("Content-Type", "text/plain")
   #     with open(filename) as sample:
   #         self.write(sample.read())

    def post(self):
        self.set_header("Content-Type", "text/plain")
        if not os.path.isfile('apply/ApplyForm.csv'):
        	with open('apply/ApplyForm.csv', 'a') as template:
        		template.write('name' + ',' + 'cellphone' + ',' + 'reason' + '\n')
        with open('apply/ApplyForm.csv', 'a') as template:
            template.write(self.get_body_argument("name") + ',' + self.get_body_argument("cellphone") + ',' + self.get_body_argument("reason") + '\n')
            self.write('ok')


#r'\apply\ApplyForm.csv'

        #以下均为套路

def main():
    if not os.path.isdir('apply'):
        os.mkdir('apply') 
    app = tornado.web.Application([
        (r"/",ApplyFormHandler),
        (r"/apply",FileHandler)
#        (r"/myform/([0-9]+)",FileHandler),
#        (r"/list",ListHandler)
        ])
    app.listen(1234)
    tornado.ioloop.IOLoop.instance().start()

if __name__=="__main__":
    main()