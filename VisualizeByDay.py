import matplotlib.pyplot as plt
import Variables as prep
import pandas as pd
import shutil
import os

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday']
mapping = {day: i for i, day in enumerate(days)}

d = pd.read_csv('data.csv', encoding = "utf-8")
text_counts = d.groupby(['weekday', 'person'])['text'].count().reset_index(name='count')

right = text_counts.loc[text_counts['person'] == prep.rightName]
left = text_counts.loc[text_counts['person'] == prep.leftName]

right = right['count'].reset_index(name='count')
left = left['count'].reset_index(name='count')

right = right.drop(['index'], axis=1)
left = left.drop(['index'], axis=1)

x = text_counts.iloc[:,0]
x = x.drop_duplicates()
x = x.reset_index(drop=True)

key = x.map(mapping)
x = x.iloc[key.argsort()]

ax = plt.subplot(111)

ax.bar(x, right['count'], color='lightskyblue', bottom=left['count'])
ax.bar(x, left['count'], color='lightcoral')
ax.legend(labels=['Me', 'You'], loc="upper right", ncol=1, bbox_to_anchor=(1.3, 1))

plt.xticks(x, rotation='70')

plt.subplots_adjust(left=0.12, right=0.79, top=0.95, bottom=0.22)
plt.margins(x=0)

plt.xlabel('Day')
plt.ylabel('Text Count')
plt.title('Messages Sent Per Day')

dir_path = os.path.dirname(os.path.realpath(__file__))

try:
    os.mkdir(dir_path + "\Data")
except OSError:  
    print ("Directory Already Exists")
else:  
    print ("Successfully created the directory")

shutil.rmtree('__pycache__')
plt.savefig(dir_path + '\Data\PerDayMessagesBAR.png')
