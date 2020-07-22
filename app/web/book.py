from flask import jsonify, request
from app.web import web     #  导入蓝图

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from app.forms.book import SearchForm


# @web.route("/book/search/<q>/<page>")
# def search(q, page):

# pip3 install wtfomrs 用于参数的校验

# a = request.args.to_dict()      # 将flask的字典, 转化为python的字典

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

        if isbn_or_key == "isbn":
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)

        # return json.dumps(result), 200, {"content-type": "application/json"}
        return jsonify(result)
    else:
        return jsonify(form.errors)
