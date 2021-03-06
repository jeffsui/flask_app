#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-19 10:26:54
# @Author  : Jeff.Sui (a575350@fmr.com)
# @Link    : 
# @Version : $Id$

from flask import Flask
from flask import Flask, flash,redirect,render_template,request,session,abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)
app=Flask(__name__)
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
        # return render_template('signup.html')
    else:
        return "Hello Boss! <a href='/logout'>Logout</a>"
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    # if request.form['password'] == 'password' and request.form['username'] == 'admin':
    #     session['logged_in'] = True
    POST_USERNAME=str(request.form['username'])
    POST_PASSWORD=str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s= Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]),User.password.in_([POST_PASSWORD]))
    result = query.first()
    if result:
    	session['logged_in'] = True
    	user(POST_USERNAME)
    else:
        flash('wrong password!')
    return home()

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello,%s!</h1>'%name

@app.route('/logout')
def logout():
	session['logged_in'] = False
	return home()
@app.route('/test')
def test():
	POST_USERNAME="jumpiness1"
	POST_PASSWORD="python"

	Session = sessionmaker(bind=engine)
	s= Session()
	query = s.query(User).filter(User.username.in_([POST_USERNAME]),User.password.in_([POST_PASSWORD]))
	result = query.first()
	print type(result)
	if result:
		return "Object found"
	else:
		return "Object not found "+ POST_USERNAME+" "+POST_PASSWORD

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='127.0.0.1', port=4000)
