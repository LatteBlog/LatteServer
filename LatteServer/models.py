# -*- coding: utf-8 -*-
"""
   LatteServer admin views

   copyright: (c) 2016 by Jack Wang

"""

from LatteServer.extension import db
from werkzeug import check_password_hash, generate_password_hash

class Admin(db.Model):
	"""博客管理员"""
	__tablename__ = 'admin'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True)
	email = db.Column(db.String, unique=True)
	pwd = db.Column(db.String,)

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.pwd = generate_password_hash(password)

	def check_pwd(self, password):
		return check_password_hash(self.pwd, password)

