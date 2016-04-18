# -*- coding: utf-8 -*-
from flask import Flask

from LatteServer.extension import db
from LatteServer.views.admin import admin
import latte_setting

def create_app(config=None):
	app = Flask(__name__)
	app.config.from_object(latte_setting)
	
	db.init_app(app)

	app.register_module(admin)

	return app