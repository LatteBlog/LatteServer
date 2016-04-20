# -*- coding: utf-8 -*-
"""LatteServer"""
from LatteServer import create_app

application = create_app()

if __name__ == "__main__":
	application.run()