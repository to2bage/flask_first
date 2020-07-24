# webserver的概念  java php nginx apache tomcat iis
# app.run()使用的是单进程, 单线程处理请求
#Local: 使用字典的方式实现的线程隔离
#LocalStack: 封装了Local, 实现了线程隔离的栈

"""
from werkzeug.local import Local
from threading import Thread
import time

my_obj = Local()
my_obj.b = 1


def worker():
    my_obj.b = 2
    print("in new thread b is ", my_obj.b)

new_t = Thread(target=worker)
new_t.start()
time.sleep(1)

print("in main thread b is ", my_obj.b)
"""

from werkzeug.local import LocalStack

s = LocalStack()
s.push(1)
print(s.top)