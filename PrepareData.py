import Variables as v
import datetime as dt
import pandas as pd
import csv
import os

with open('texts.csv', encoding='utf-8') as source:
	rdr = csv.reader(source)
	with open('result.csv', 'w', encoding='utf-8') as result:
		wtr = csv.writer(result)
		for r in rdr:
			if r:
				wtr.writerow((r[0],r[1],r[2],r[3],r[4]))

d = pd.read_csv('result.csv', encoding='utf-8')
d['Date'] = pd.to_datetime(d['Date'])
d['Received'] = d['Received'].fillna(v.leftName)
d['Received'] = d['Received'].str.replace('Yes', v.rightName)
d = d.rename(index=str, columns={'Date': 'dateTime', 'Received': 'person'})
d = d.assign(date = d['dateTime'].dt.strftime('%m/%d/%Y'))
d = d.assign(hour = d['dateTime'].dt.strftime('%H'))
d = d.assign(year = d['dateTime'].dt.strftime('%Y'))
d = d.assign(month = d['dateTime'].dt.strftime('%m'))
d = d.assign(day = d['dateTime'].dt.strftime('%d'))
d = d.assign(weekday = d['dateTime'].dt.strftime('%A'))
d = d.drop(['iMessage'], axis=1)
d = d.drop(['Sender'], axis=1)
d = d.rename(index=str, columns={"Text": "text"})

d.to_csv('data.csv', encoding='utf-8')

os.remove('result.csv')
