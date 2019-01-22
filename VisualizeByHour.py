import matplotlib.pyplot as plt
import Variables as prep
import pandas as pd
import shutil
import os

d = pd.read_csv('data.csv', encoding = "utf-8")
text_counts = d.groupby(['hour', 'person'])['text'].count().reset_index(name='count')

left2 = text_counts.loc[text_counts['person'] == prep.leftName].drop(['person'], axis = 1).reset_index(drop=True)
right2 = text_counts.loc[text_counts['person'] == prep.rightName].drop(['person'], axis = 1).reset_index(drop=True)

left2.index = left2['hour']
right2.index = right2['hour']

left = pd.DataFrame({'hour': range(0, 24), 'count': 0})
left.index = left['hour']
right = pd.DataFrame({'hour': range(0, 24), 'count': 0})
right.index = right['hour']

left['count'] = left2['count']
right['count'] = right2['count']

left = left.fillna(0)
right = right.fillna(0)

left = left.drop('hour', 1).reset_index()
right = right.drop('hour', 1).reset_index()

x = right.iloc[:,0]
x = x.drop_duplicates()
x = x.reset_index(drop=True)

ax = plt.subplot(111)

ax.bar(x, right['count'], color='lightskyblue', bottom=left['count'])
ax.bar(x, left['count'], color='lightcoral')
ax.legend(labels=['Me', 'You'], loc="upper right", ncol=1, bbox_to_anchor=(1.3, 1))

plt.xticks(x, rotation='70')

plt.subplots_adjust(left=0.12, right=0.79, top=0.95, bottom=0.22)
plt.margins(x=0)

plt.xlabel('Hour')
plt.ylabel('Text Count')
plt.title('Texts by Hour')

dir_path = os.path.dirname(os.path.realpath(__file__))

try:
    os.mkdir(dir_path + "\Data")
except OSError:  
    print ("Directory Already Exists")
else:  
    print ("Successfully created the directory")

shutil.rmtree('__pycache__')
plt.savefig(dir_path + '\Data\PerHourMessagesBAR.png')
