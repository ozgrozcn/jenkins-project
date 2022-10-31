from datetime import datetime
time = datetime.strftime(datetime.today(),'%d')

if int(time) > 15: print("bööö :*")
else: 
  for i in range(int(time),0,-1): 
    print("{}. day is invalid".format(i))
