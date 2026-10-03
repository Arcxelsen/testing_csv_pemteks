import pandas as pd
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/Arcxelsen/testing_csv_pemteks/refs/heads/main/gt_wiki_TP.csv"
df = pd.read_csv(url)
pd.set_option('display.max_rows', None)

#lower
colomn = "Item_Name"
data_csv = "\n".join(df[colomn].dropna().astype(str))
hasil = str.lower(data_csv)
print(hasil)

#remove url
def remove_rls(text):
    text = re.sub(r'https?\/\/S+', '',  str(text)) # remove the hyperlink
    text = re.sub(r'http\S+', '',  str(text)) # remove the hyperlink
    text = re.sub(r'www\S+', '',  str(text)) # remove the www
    text = re.sub(r'\S+@\S+', '', str(text)) # remove the email
    return text

hasil_rurl = remove_rls(df)
print(hasil_rurl)

df.info()
#wordcloud
text = ' '.join(df['Item_Name'].dropna().astype(str))
wordcloud = WordCloud(width=1000, height=800, background_color='white', max_words=1000).generate(text)

plt.figure(figsize=(6, 4))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()