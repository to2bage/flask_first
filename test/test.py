from flask import Flask, current_app


app = Flask(__name__)

# ctx = app.app_context()
# ctx.push()
#
# a = current_app
# a.config.from_object("app.secure")
# print(a.config["DEBUG"])
#
# ctx.pop()

"""
class A:
    def __enter__(self):
        a = 1
        return a

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 用于 回收资源, 处理异常.. 
        b = 2

# A()被成为上下文表达式, 目的是生成上下文管理器对象
# A被成为上下文管理器
with A() as obj_A:
    print(obj_A)  # 是__enter__的返回值 1
    pass
"""

class MyResource:
    def __enter__(self):
        print("connect to source")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # return True: with内部有异常抛出, 则[不会]再向with的外部抛出异常
        # return False:with内部有异常抛出, 则[会]再向with的外部抛出异常
        # 默认返回Fasle
        if exc_tb:
            print("处理异常")
        else:
            print("没有异常")
        return True

    def query(self):
        print("请求数据")


with MyResource() as resource:
    1/0     #  直接跳转到__exit__()
    resource.query()