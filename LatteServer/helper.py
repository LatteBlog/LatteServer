# -*- coding: utf-8 -*-
"""
   LatteServer admin views

   copyright: (c) 2016 by Jack Wang

"""
from LatteServer.models import Admin

def check_email(email):
	admin = Admin.query.filter_by(email=email).first()
	return not admin

def check_username(username):
	admin = Admin.query.filter_by(username=username).first()
	return not admin