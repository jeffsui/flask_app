#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-19 10:24:23
# @Author  : Jeff.Sui (a575350@fmr.com)
# @Link    : 
# @Version : $Id$

from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
	return "Hello World!"
if __name__ == '__main__':
	app.run(host='127.0.0.1',port=4000)