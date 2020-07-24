from app.libs._http import HTTP
from flask import current_app


# 模型层: MVC中的M层
class YuShuBook:
    # 原始的数据是存储在YushuBook中的

    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)      # type(result) => dict
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config["PER_PAGE_NUM"], YuShuBook.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def calculate_start(self, page):
        return (page-1) * current_app.config["PER_PAGE_NUM"]

    def __fill_single(self, data):
        if data is not None:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        if data is not None:
            self.total = data["total"]
            self.books = data["books"]