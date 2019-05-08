import json
from  datetime import datetime
from datetime import date
import pymongo
import pickle

# Get today's date and first day of month
today = date.today()
date = datetime.now()
curmonth = today.strftime("%m")
curyear = today.strftime("%Y")
firstdate = datetime(int(curyear),int(curmonth),1)

# Get current usage from mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["cmpe272"]
mycol = mydb["usage"]

# get total usage of the month
total = 0
for d in mycol.find():
    if d['date']<=date and d['date']>= firstdate:
        total += int(d['units'])
# print(total)

# Load regression model
pickle_in = open('price-forecast-model.pickle','rb')
model = pickle.load(pickle_in)

# predict bill for total monthly usage
predictValue = model.predict([[total]])[0][0]
print(predictValue)