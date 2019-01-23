import matplotlib.pyplot as plt
import Variables as prep
import pandas as pd
import shutil
import random
import os

d = pd.read_csv('data.csv', encoding = "utf-8")
df = pd.DataFrame({'person': d['person'], 'text': d['text']})

left = df.loc[df['person'] == prep.leftName].drop(['person'], axis = 1).reset_index(drop=True)
right = df.loc[df['person'] == prep.rightName].drop(['person'], axis = 1).reset_index(drop=True)

leftMax = max(left['text'].map(str).apply(len))
rightMax = max(right['text'].map(str).apply(len))

combinedMaxList = [rightMax, leftMax] 
combinedMax = pd.DataFrame({'max': combinedMaxList})

x = ['Me', 'You']

plt.barh(x, (combinedMax['max'].values), align='center', color=('lightskyblue', 'lightcoral'))	

plt.subplots_adjust(left=0.12, right=0.95, top=0.95, bottom=0.22)

plt.xlabel('Person')
plt.ylabel('Message Length')
plt.title('Longest Message')

dir_path = os.path.dirname(os.path.realpath(__file__))

try:
    os.mkdir(dir_path + "\Data")
except OSError:  
    print ("Directory Already Exists")
else:  
    print ("Successfully created the directory")

shutil.rmtree('__pycache__')
plt.savefig(dir_path + '\Data\PerPersonMessageLengthBAR.png')
