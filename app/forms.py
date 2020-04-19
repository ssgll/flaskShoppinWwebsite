# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
import re


# 用户注册表单
class userRegisterForm(FlaskForm):
    # 用户名
    username = StringField(
        label="username",
        validators=[DataRequired()]
    )
    # 密码
    password = PasswordField(
        label="password",
        validators=[DataRequired()]
    )
    # 确认密码
    passwordConfirm = PasswordField(
        label="passwordConfirm",
        validators=[DataRequired(), EqualTo("password", "两次密码不一致")]
    )
    # 手机号
    phone = StringField(
        label="phone",
        validators=[DataRequired()],
    )
    # 提交
    submit = SubmitField(
        label="submit"
    )

    # 用户名校验
    def usernameValidator(username):
        pattern = "^[a-z0-9_]{3,16}$"
        match = len(re.findall(pattern, username))
        if match == 0:
            return "用户名不符合规范,只能由数字、字母和下划线组成,且大于2位"

    # 密码校验
    def passwordValidator(password, passwordConfirm):
        pattern = "^[a-z0-9_-]{6,18}$"
        if password != passwordConfirm:
            return "两次密码不一致"
        match = len(re.findall(pattern, password))
        if match == 0:
            return "密码不符合规范,只能由数字、字母和下划线组成,且大于6位"

    # 手机号校验
    def phoneValidator(phone):
        pattern = "1\d{10}"
        match = len(re.findall(pattern, phone))
        if match == 0:
            return "手机号不符合规范"


# 用户登录表单
class userLoginForm(FlaskForm):
    # 用户名
    username = StringField(
        label="username",
        validators=[DataRequired()],
        render_kw={
            "type":"text",
            "value":"用户名",
            "onFocus":"this.value=''",
            "onBlur":"if (this.value == ''){ this.value = '用户名' }",
            "required":"",
        }
    )
    # 密码
    password = PasswordField(
        label="password",
        validators=[DataRequired()],
        render_kw={
            "type":"password",
            "value":"",
            "onFocus":"this.value=''",
            "onBlur":"if (this.value == ''){ this.value = '' }",
            "required":"",
        }
    )
    # 提交
    submit = StringField(
        label="登录",
        render_kw={
            "type":"submit",
            "value":"登录"
        }
    )