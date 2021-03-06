# -*- coding: utf-8 -*-
"""
   LatteServer admin views

   copyright: (c) 2016 by Jack Wang

"""
from flask import Module, session, request, jsonify
from LatteServer.extension import db
from LatteServer.models import Admin
from LatteServer.helper import check_email, check_username

admin = Module(__name__)

@admin.route('/login', methods=['GET','POST'])
def login():
	message = None
	code = None
	username = request.form['username']
	pwd = request.form['password']
	result = {}
	if 'logged' in session and session['logged']:
		code = '2'
		message = '已经登陆，请先登出'
	else:
		if username and username != '':
			if pwd and pwd != '':
				admin = Admin.query.filter_by(username=username).first()
				if not admin:
					message = '用户名无效'
					code = '3'
				elif not admin.check_pwd(pwd):
					message = '密码错误'
					code = '4'
				else:
					session['logged'] = admin.id
					code = '1'
					message = admin.username
			else:
				code = '5'
				message = '密码不能为空'
		else:
			code = '6'
			message = '用户名不能为空'

	result['code'] = code
	result['message'] = message
	return jsonify(result)

@admin.route('/checkemail')
def checkemail():
	email = request.args.get('email')
	result = {}
	result['state'] = check_email(email)
	return jsonify(result) 

@admin.route('/checkusername')
def checkusername():
	username = request.args.get('username')
	result = {}
	result['state'] = check_username(username)
	return jsonify(result)

@admin.route('/register', methods=['GET','POST'])
def register():
	message = None
	code = None
	result = {}
	username = request.args.get('username')
	email = request.args.get('email')
	password = request.args.get('password')
	if email and email == '':
		code = '0'
		message = '邮箱不能为空'
	elif username and username == '':
		code = '2'
		message = '用户名不能为空'
	elif password and password == '':
		code = '3'
		message = '密码不能为空'
	else:
		if(check_email(email)):
			if(check_username(username)):
				db.session.add(Admin(username,email,password))
				db.session.commit()
				code = '1'
				message = 'ok'
			else:
				code = '4'
				message = '用户名已被注册'
		else:
			code = '5'
			message = '邮箱已被注册'
	
	result['code'] = code
	result['message'] = message
	return jsonify(result)

@admin.route('/logout')
def logout():
	code = None
	message = None
	result = {}
	if 'logged' not in session or not session['logged']:
		code = '0'
		message = '还没有登录'
	else:
		session.pop('logged', None)
		code = '1'
		message = 'ok'
	result['code'] = code
	result['message'] = message
	return jsonify(result)

@admin.route('/getuser')
def getuser():
	username = None
	email = None
	result = {}
	if 'logged' in session and session['logged']:
		adminid = session['logged']
		if adminid:
			admin = Admin.query.filter_by(id=adminid).first()
			username = admin.username
			email = admin.email
			result['username'] = username
			result['email'] = email
	
	return jsonify(result)
