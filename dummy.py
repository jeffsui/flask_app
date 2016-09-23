#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-19 10:57:48
# @Author  : Jeff.Sui (a575350@fmr.com)
# @Link    : 
# @Version : $Id$

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///tutorial.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("admin","password")
session.add(user)
 
user = User("python","python")
session.add(user)
 
user = User("jumpiness","python")
session.add(user)
 
# commit the record the database
session.commit()
 
session.commit()
