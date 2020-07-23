from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy


# 自动化的数据库映射 sqlalchemy
# install flask-sqlalchemy


# 实例化sqlalchemy对象
db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), nullable=False, default="未名")
    binding = Column(String(20))  # 包装
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))
    pass