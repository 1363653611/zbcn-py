#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import request, Flask, render_template

__author__ = 'zbcn8'

mvc_app = Flask(__name__)

@mvc_app.route("/", methods=['GET','POST'])
def home():
	return render_template('home.html')

@mvc_app.route('/sign',methods=['GET'])
def sign_form():
	return render_template('form.html')
@mvc_app.route('/signin', methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	# 需要从request对象读取表单内容：
	if username == 'admin' and password == 'password':
		return render_template('sign-ok.html', username=username)
	return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    mvc_app.run()