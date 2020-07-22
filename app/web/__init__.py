__author__ = "to2bage"


from flask import Blueprint

#  蓝图的实例化
web = Blueprint("web", __package__)        #  (蓝图的名字, 所在模块的名字)

# 导入web这个蓝图下的视图, 且必须写在蓝图实例化到下方
from app.web import book