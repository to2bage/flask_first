__author__ = "to2bage"

from flask import Flask
from app.models.book import db


def register_blueprint(app: Flask):
    from app.web import web
    from app.api import api
    app.register_blueprint(web)
    app.register_blueprint(api)


def create_app():
    app = Flask(__name__)
    # 设置配置文件
    app.config.from_object("app.secure")
    app.config.from_object("app.setting")
    # 注册蓝图
    register_blueprint(app)
    # 关联数据库
    db.init_app(app)
    # db.create_all(app=app)     # 将定义的所有model映射到数据库中
    with app.app_context():
        db.create_all()
    return app      #  返回核心对象