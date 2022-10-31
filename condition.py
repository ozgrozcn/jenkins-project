from datetime import datetime
tm = datetime.strftime(datetime.today(),'%d')

if int(tm) > 15: print("bööö")
else: 
  for i in range(int(tm),0,-1): 
    print("{}. day is invalid".format(i))
