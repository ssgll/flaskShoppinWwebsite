# -*- coding: utf-8 -*-

from flask import Flask
from setting import config
from app.urls import userBlueprint
from app.models import user, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

# 生成app
app = Flask(
    __name__,
    template_folder=config["Default"].TEMPLATE_FLODER,
    static_folder=config["Default"].STATIC_FLODER
)
# 加载配置文件
app.config.from_object(config["Default"])

# 注册蓝图
# app.register_blueprint(indexblueprint)  # index蓝图
app.register_blueprint(userBlueprint)  # 用户蓝图

# 绑定数据库
db.init_app(app=app)
# 映射数据库
manager = Manager(app)
Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)  # 创建数据库映射命令
manager.add_command("start", Server(host=app.config["HOST"], port=app.config["PORT"],
                                    use_debugger=app.config['DEBUG']))  # 创建启动命令

if __name__ == "__main__":
    manager.run()
