import json
from datetime import datetime
import sys 


max_heart_rate=200
fifty = 0.5*max_heart_rate
sixty = 0.6*max_heart_rate
seventy= 0.7*max_heart_rate
eighty= 0.8*max_heart_rate

fitbit_dict={}
final_scores={}

if len(sys.argv) < 2:
	print("Please enter json file name as argument")
	sys.exit()
else:	
	with open(sys.argv[1]) as f:
  		data = json.load(f)


for key in data:
    datetime_object = datetime.strptime(key['dateTime'], '%m/%d/%y %H:%M:%S')
    fitbit_dict.setdefault(datetime_object.date(), []).append(key['value']['bpm'])


for x, y in fitbit_dict.items():
	score=0
	for i in y:
		if i >= fifty and i < sixty:
			score+=1
		if i >= sixty and i < seventy:
			score+=2
		if i >= seventy and i < eighty:
			score+=3
		if i >= eighty:
			score+=4
	final_scores[datetime_object.date()] = score

for x,y in final_scores.items():
	print(x, "Score:" + str(y))

