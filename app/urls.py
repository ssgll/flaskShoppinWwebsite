# -*- coding: utf-8 -*-

from app import indexblueprint, userBlueprint
from app.views.user import userRegister, userLogin

# indexblueprint.add_url_rule("/", endpoint=None, view_func=indexview, methods=["GET", "POST"])


# 添加userRegister路由
userBlueprint.add_url_rule("/userRegister", endpoint="userRegister", view_func=userRegister, methods=["GET", "POST"])
# 添加userLogin路由
userBlueprint.add_url_rule("/userLogin", endpoint="userLogin", view_func=userLogin, methods=["GET", "POST"])