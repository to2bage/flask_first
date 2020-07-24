from flask import jsonify, request, render_template, flash
from app.web import web     #  导入蓝图
import json

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from app.view_models.book import BookViewModel, BookCollection

# @web.route("/book/search/<q>/<page>")
# def search(q, page):

# pip3 install wtfomrs 用于参数的校验

# a = request.args.to_dict()      # 将flask的字典, 转化为python的字典

books = BookCollection()

@web.route("/book/search")
def search():
    # q = request.args["q"]
    # page = request.args["page"]

    # 使用第三方wtforms校验参数: q 和 page
    form = SearchForm(request.args)
    if form.validate():
        # 验证成功
        q = form.q.data.strip() # 从form中获取q值
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()        #  YuShuBook对象中存储了原始的数据

        if isbn_or_key == "isbn":
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)
        books.fill(yushu_book, q)       #  使用view_model处理原始数据, books包含了要展示的数据

        # return json.dumps(result), 200, {"content-type": "application/json"}
        # return jsonify(books)
        # return json.dumps(books, default=lambda obj: obj.__dict__)
        # return render_template("search_result.html", books=books)
    else:
        # return jsonify(form.errors)
        flash("搜索的关键字不符合要求, 请重新输入关键字")
    return render_template("search_result.html", books=books)



@web.route("/book/<isbn>/detail")
def book_detail(isbn):
    pass




#  以下是用于测试的
@web.route("/test")
def test_template():
    r = {
        "name": "to2bage",
        "age": 45
    }
    flash("你好, Flask", category="error")      # 定义消息闪现, 在模板文件test.html中使用
    flash("Hello 发了十块", category="warning")
    # return jsonify(r)
    return render_template("test.html", data=r)
