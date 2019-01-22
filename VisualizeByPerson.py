import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

d = pd.read_csv('data.csv', encoding = "utf-8")
text_counts = d.groupby('person')['text'].count().reset_index(name='count')

x = text_counts.iloc[:,0]
y = text_counts.iloc[:,1]

fig = plt.figure(0)
ax = fig.gca()

def absolute_value(val):
    a  = np.round(val/100.*y.sum(), 0)
    a = a.astype(int)
    b = (a/(d['text'].count())*100)
    b = b.astype(int)
    return a.astype(str) + " (" + b.astype(str) + "%)"

ax.pie(y, labels=["", ""], autopct=absolute_value, colors=['lightskyblue', 'lightcoral'])
ax.axis('equal')
ax.legend(title="People", labels=["Me", "You"])

plt.subplots_adjust(left=0, right=1, top=0.9, bottom=0.1)
plt.margins(x=0)

plt.title('Total Messages Sent')

dir_path = os.path.dirname(os.path.realpath(__file__))

try:
    os.mkdir(dir_path + "\Data")
except OSError:  
    print ("Directory Already Exists")
else:  
    print ("Successfully created the directory")

plt.savefig(dir_path + '\Data\TotalMessagesPIE.png')
