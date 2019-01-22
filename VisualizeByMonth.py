import matplotlib.pyplot as plt
import Variables as prep
import pandas as pd
import calendar
import shutil
import os

d = pd.read_csv('data.csv', encoding = "utf-8")
text_counts = d.groupby(['month', 'person'])['text'].count().reset_index(name='count')

days_count = d['dateTime'].dropna()

yearStart = (pd.to_datetime(days_count.reset_index(name='count').iloc[:,1].head(1)))[0].year

left2 = text_counts.loc[text_counts['person'] == prep.leftName].drop(['person'], axis = 1).reset_index(drop=True)
right2 = text_counts.loc[text_counts['person'] == prep.rightName].drop(['person'], axis = 1).reset_index(drop=True)

left2.index = left2['month']
right2.index = right2['month']

left = pd.DataFrame({'month': range(1, 13), 'count': 0})
left.index = left['month']
right = pd.DataFrame({'month': range(1, 13), 'count': 0})
right.index = right['month']

left['count'] = left2['count']
right['count'] = right2['count']

left = left.fillna(0)
right = right.fillna(0)

left = left.drop('month', 1).reset_index()
right = right.drop('month', 1).reset_index()

x = right.iloc[:,0]
x = x.drop_duplicates()
x = x.reset_index(drop=True)

t = []
for i in x:
    if (i != 12):
        l = int(i / 12)
        i = int(i % 12)
    t.append((str(calendar.month_abbr[int(i)]) + "\n" + str(l + yearStart)))

ax = plt.subplot(111)

ax.bar(x, right['count'], color='lightskyblue', bottom=left['count'])
ax.bar(x, left['count'], color='lightcoral')
ax.legend(labels=['Me', 'You'], loc="upper right", ncol=1, bbox_to_anchor=(1.3, 1))

plt.xticks(x, labels=t, rotation='0')

plt.subplots_adjust(left=0.12, right=0.79, top=0.95, bottom=0.22)
plt.margins(x=0)

plt.xlabel('Month')
plt.ylabel('Text Count')
plt.title('Messages Sent Per Month')

dir_path = os.path.dirname(os.path.realpath(__file__))

try:
    os.mkdir(dir_path + "\Data")
except OSError:  
    print ("Directory Already Exists")
else:  
    print ("Successfully created the directory")

shutil.rmtree('__pycache__')
plt.savefig(dir_path + '\Data\PerMonthMessagesBAR.png')
