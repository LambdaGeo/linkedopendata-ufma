from wordcloud import WordCloud
import json, requests
from pylab import *
from stop_words import get_stop_words

stop_words = get_stop_words('pt')
stop_words.append("usando")
stop_words.append("utilizando")
stop_words.append("área")




url = "https://dados-abertos-ufma.herokuapp.com/api/v01/docentes"
text = ""
for ano in range(2014,2017):
    r = requests.get(url).json()
    dados = r["data"]
    for m in dados:
        text = text + m["areas_de_interesse"].upper()

wc = WordCloud(background_color="white",max_words=10000, stopwords=stop_words, margin=0,
random_state=1).generate(text)

plt.figure()
plt.imshow(wc)
plt.axis("off")
plt.show()




