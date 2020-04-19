# -*- coding: utf-8 -*-

import mysql.connector
from datetime import timedelta
import os


class Config(object):
    DEBUG = True  # 调试模式
    PORT = 80  # 端口
    HOST = "127.0.0.1"  # ip
    SECRET_KEY = "ssgll"  # session秘钥
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://ssgll:383687@127.0.0.1:3306/ztz?charset=utf8"  # 数据库url
    SQLALCHEMY_ECHO = False  # 数据库调试信息
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 一般关闭
    PERMENENT_SESSION_LEFTTIME = timedelta(days=1)  # session过期时间
    # SESSION_COOKIE_NAME="session",  # 存储cookie
    # JSONFLY_MIMETYPE="application/json",  # jsonfly返回类型
    APPLICATION_ROOT="/" # 项目目录
    # TESTING=True  # 测试模式
    BASE_DIR=os.getcwd()
    STATIC_FLODER=os.path.join(BASE_DIR, "static")  # static文件夹
    TEMPLATE_FLODER=os.path.join(BASE_DIR, "templates")  # template文件夹


class Development(Config):
    pass


class Testing(Config):
    pass


config = {
    "Config" : Config,
    "Development": Development,
    "Testing": Testing,
    "Default": Config,
}