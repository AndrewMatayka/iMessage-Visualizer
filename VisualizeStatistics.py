import pandas as pd
import os

d = pd.read_csv('data.csv', encoding = "utf-8")

test = d['text'].str.split()
test = test.dropna()
test = test.reset_index(drop=True)

test2 = d.groupby('date')['text'].count().reset_index(name='count')

test3 = test2.sort_values(by='count')
test3 = str(test3.tail(1).iloc[0,0]) + " (" + str(test3.tail(1).iloc[0,1]) + ")"

days_count = d['dateTime']
days_count = days_count.dropna()

monthStart = days_count.reset_index(name='count')

initial = pd.to_datetime(days_count.head(1).iloc[0])
final = pd.to_datetime(days_count.tail(1).iloc[0])
days_count = (final - initial)
days_count = days_count.days

monthStart = monthStart.head(1).iloc[0,1]
monthStart = pd.to_datetime(monthStart)

sumcount = 0
p = 0

for i in test:
    for x in test[p]:
        sumcount += 1
    p += 1

avg = (sumcount / d['text'].count())
avg2 = ((d['text'].count()) / (len(test2)))

dir_path = os.path.dirname(os.path.realpath(__file__))

try:
    os.mkdir(dir_path + "\Data")
except OSError:  
    print ("Directory Already Exists")
else:  
    print ("Successfully created the directory")

f= open(dir_path + "\Data\Statistics.txt","w+")
f.write("Start Date: " + monthStart.strftime('%m/%d/%Y') + "\n")
f.write("Most Active Date: " + test3 + "\n")
f.write("")
f.write(str(days_count) + " Days\n")
f.write(str(d['text'].count()) + " Messages\n")
f.write(str(sumcount) + " Words\n")
f.write("")
f.write(str(avg) + " Average Message Word Length\n")
f.write(str(avg2) + " Average Messages Per Day of Texting\n")
f.close()
