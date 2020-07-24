"""
Create Time: 2020/7/24 08:17
Author: to2bage
"""

class _BookViewModel:

    returned = {
        "books": [],
        "total": 0,
        "keyword": ""
    }

    @classmethod
    def package_single(cls, data, keyword):
        if data is not None:
            cls.returned["total"] = 1
            cls.returned["keyword"] = keyword
            cls.returned["books"] = [cls.__cut_book_data(data)]
        return cls.returned

    @classmethod
    def package_collection(cls, data, keyword):
        if data is not None:
            cls.returned["total"] = data["total"]
            cls.returned["keyword"] = keyword
            cls.returned["books"] = [cls.__cut_book_data(book) for book in data["books"]]
        return cls.returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            "title": data["title"],
            "publisher": data["publisher"],
            "pages": data["pages"] or "",
            "author": ", ".join(data["author"]),
            "price": data["price"],
            "summary": data["summary"] or "",
            "image": data["image"]
        }
        return book



class BookViewModel:
    def __init__(self, book):
        # 处理当个数据
        self.title = book["title"]
        self.publisher = book["publisher"]
        self.pages = book["pages"]
        self.author = book["author"]
        self.price = book["price"]
        self.summary = book["summary"]
        self.image = book["image"]
        pass


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ""

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]
