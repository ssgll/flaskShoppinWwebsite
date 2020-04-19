# -*- coding: utf-8 -*-

from flask import render_template, request, flash, session, redirect, url_for
from app.forms import userRegisterForm, userLoginForm
from app.models import user, db


# 用户注册视图
def userRegister():
    global searchStatus
    errStatus = False
    err = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        passwordConfirm = request.form.get("passwordConfirm")
        phone = request.form.get("phone")
        # 校验
        validators = [
            userRegisterForm.usernameValidator(username),
            userRegisterForm.passwordValidator(password, passwordConfirm),
            userRegisterForm.phoneValidator(phone)
        ]
        # 去除重复值
        validators = list(set(validators))
        for val in validators:
            if val is not None:
                flash(val)
                break
        # 是否无错误信息
        if len(validators) == 1 and validators[0] is None:
            users = user(username, password, phone)  # 创建ORM结构
            try:
                username = user.query.filter_by(username=username).one()  # 查询用户名
                if username is not None:
                    searchStatus = False
            except BaseException:
                searchStatus = True
            if searchStatus:
                try:
                    db.session.add(users)
                    db.session.commit()  # 提交到数据库进行持久化
                    appendStatus = True
                except BaseException:
                    db.session.rollback()
                    appendStatus = False
            if searchStatus and appendStatus:
                err ="注册成功,即将跳转到登录界面"
                errStatus = True
            elif not searchStatus:
                err = "该用户名已被使用"
            else:
                err = "注册失败"
        flash(err)
        # 重定向到登录页面
        if errStatus:
            return redirect(url_for("userBlueprint.userLogin"))
    return render_template("./user/register.html", form=userRegisterForm())


# 用户登录视图
def userLogin():
    if request.method == "POST":
        # 获取表单
        username = request.form.get("username")
        password = request.form.get("password")
        error = None
        usernameTemp = None
        passwordTemp = None
        try:
            usernameTemp = user.query.filter_by(username=username).one().username  # 用户名校验
        except BaseException:
            error = "用户名错误"
        if usernameTemp is not None:
            try:
                passwordTemp = user.query.filter_by(username=username).one().password  # 密码校验
            except:
                error = "密码错误"
        if error is not None:
            flash(error)
        if password == passwordTemp:
            session["username"] = username
    return render_template("./user/login.html", form=userLoginForm())