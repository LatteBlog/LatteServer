# -*- coding: utf-8 -*-
"""默认运行于localhost 5100端口"""
from LatteServer import create_app

if __name__ == "__main__":
	app = create_app()
	app.run(host="0.0.0.0", port=5100)