#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-19 10:06:25
# @Author  : Jeff.Sui (a575350@fmr.com)
# @Link    : 
# @Version : $Id$
from setuptools import setup
 
setup(name='TodoApp',
      version='1.0',
      description='Todo Application',
      author='Shekhar Gulati',
      author_email='',
      url='http://www.python.org/sigs/distutils-sig/',
     install_requires=['flask==0.10.1','flask-login==0.2.7','sqlalchemy==0.8.2','flask-sqlalchemy==1.0'],
     )