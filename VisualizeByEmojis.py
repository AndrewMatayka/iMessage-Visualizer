import matplotlib.pyplot as plt
import pandas as pd
import regex
import emoji
import mpld3
import os

d = pd.read_csv('data.csv', encoding = "utf-8")

wordlist = []
strings = []

for x in d['text']:
        strings.append(x)

data = regex.findall(r'\X', str(strings))

for word in data:
        if any(char in emoji.UNICODE_EMOJI for char in word):
                wordlist.append(word)

df = pd.DataFrame({'Emojiwordlist})

df = df.groupby('Emoji')['Emoji'].count().sort_values(ascending=False).reset_index(name='count')

fig, ax = plt.subplots()
ax.bar(df.iloc[:,0].head(10), df.iloc[:,1].head(10))

x = df.iloc[:,0].head(10)

ax.set_xticks(x)
ax.set_xticklabels(x)

dir_path = os.path.dirname(os.path.realpath(__file__))

try:
    os.mkdir(dir_path + "\Data")
except OSError:  
    print ("Directory Already Exists")
else:  
    print ("Successfully created the directory")

mpld3.save_html(fig, './Data/TopEmojis.html')