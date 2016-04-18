# -*- coding: utf-8 -*-
from __future__ import with_statement
import os
from LatteServer.extension import db
from LatteServer import create_app

app = create_app()

with app.test_request_context():
	db.create_all()

print "数据库初始化完成，位于 %s" % app.config['SQLALCHEMY_DATABASE_URI']
