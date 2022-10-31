#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
tm = datetime.strftime(datetime.today(),'%d')
print(datetime.strftime(datetime.today(),'%Y-%m-%d'))
if int(tm) > 31: print("bööö :*")
else: 
  for i in range(int(tm),0,-1): 
    print("{}. day is invalid".format(i))
