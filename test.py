# -*- coding:utf-8 -*-



post = open('post1', 'w')
post.write('123')
post = open('post1')
print post.read()
post.close()



with open('post2', 'w') as sample:
  sample.write('234')


with open('post2') as sample:
  print sample.read()
