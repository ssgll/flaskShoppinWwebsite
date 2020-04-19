# -*- coding: utf-8 -*-

from flask import Blueprint


# 注册index蓝图
indexblueprint = Blueprint("indexBlueprint", __name__)


# 用户user蓝图
userBlueprint = Blueprint("userBlueprint", __name__)