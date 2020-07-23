from flask import Flask

from app.libs.helper import is_isbn_or_key

app = Flask(__name__)
# 设置配置文件
app.config.from_object("config")

# @app.route("/hello", methods=["GET", "POST"])
# def hello():
#     # 视图函数返回Response对象或元组: 内容, status code, headers
#     headers = {
#         "content-type": "text/plain",
#         "location": "https://www.baidu.com"
#     }
#     response = make_response("<html></html>", 301)  # 301: 重定向
#     response.headers = headers
#     return response
    # return "<html></html>" 301, headers

# 路由注册: 非装饰器的方式, 适用于基于类的视图(即插视图)的方式
# app.add_url_rule("/hello", view_func=hello)


@app.route("/book/search/<q>/<page>")
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    
    pass


if __name__ == '__main__':
    # 生产环境: nginx+uwsgi
    app.run(debug=app.config["DEBUG"],host="0.0.0.0")