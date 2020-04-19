# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

# 创建一个db对象
db = SQLAlchemy()


# 用户基本表
class user(db.Model):
    table_name = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    phone = db.Column(db.String(128))

    def __init__(self, username, password, phone):
        self.username = username
        self.password = password
        self.phone = phone

    def __repr__(self):
        return "<User %r>" % self.username