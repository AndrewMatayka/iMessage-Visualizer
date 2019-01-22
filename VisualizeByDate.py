import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import Variables as prep
import datetime as dt
import pandas as pd
import shutil
import os

locator = mdates.MonthLocator()
fmt = mdates.DateFormatter('%b\n%Y')

d = pd.read_csv('data.csv', encoding = "utf-8")
text_counts = d.groupby(['date', 'person'])['text'].count().reset_index(name='count')

days_count = d['dateTime']
days_count = days_count.dropna()

initial = pd.to_datetime(days_count.head(1).iloc[0])
final = pd.to_datetime(days_count.tail(1).iloc[0])

left2 = text_counts.loc[text_counts['person'] == prep.leftName].drop(['person'], axis = 1).reset_index(drop=True)
right2 = text_counts.loc[text_counts['person'] == prep.rightName].drop(['person'], axis = 1).reset_index(drop=True)

left2.index = left2['date']
right2.index = right2['date']

left = pd.DataFrame({'date': pd.date_range(start = initial ,end = final).strftime('%m/%d/%Y'), 'count': 0})
left.index = left['date']
right = pd.DataFrame({'date': pd.date_range(start = initial ,end = final).strftime('%m/%d/%Y'), 'count': 0})
right.index = right['date']

left['count'] = left2['count']
right['count'] = right2['count']

left = left.fillna(0)
right = right.fillna(0)

left = left.drop('date', 1).reset_index()
right = right.drop('date', 1).reset_index()

x = right.iloc[:,0]
x = x.drop_duplicates()
x = x.reset_index(drop=True)
x = pd.to_datetime(x)
x = x.dt.to_pydatetime()

ax = plt.subplot(111)

ax.bar(x, right['count'], color='lightskyblue', bottom=left['count'])
ax.bar(x, left['count'], color='lightcoral')
ax.legend(labels=['Me', 'You'], loc="upper right", ncol=1, bbox_to_anchor=(1.3, 1))

ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(fmt)

plt.xticks(rotation='0')

plt.subplots_adjust(left=0.12, right=0.79, top=0.95, bottom=0.22)
plt.margins(x=0)

plt.xlabel('Date')
plt.ylabel('Text Count')
plt.title('Messages Sent By Date')


dir_path = os.path.dirname(os.path.realpath(__file__))

try:
    os.mkdir(dir_path + "\Data")
except OSError:  
    print ("Directory Already Exists")
else:  
    print ("Successfully created the directory")

shutil.rmtree('__pycache__')
plt.savefig(dir_path + '\Data\PerDateMessagesBAR.png')