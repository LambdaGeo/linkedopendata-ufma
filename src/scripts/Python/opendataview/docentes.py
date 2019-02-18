import json, requests
from pylab import *


url = "http://dados.inova-campus.xyz/v01/organizacional/subunidades/"
r = requests.get(url)
dados = r.json()['data']

dados_plot = []

total_docentes = 0
for v in dados:
  
    url2 = "http://dados.inova-campus.xyz/v01/pessoas/docentes/?departamento="+v['nome']   
    r2 = requests.get(url2)
    dados2 = r2.json()['data']
    n = len(dados2)
    if n > 0:
        total_docentes = total_docentes + n
        dados_plot.append ({"codigo": v['codigo'], "qt":n, "nome":v['nome'] })
        
print ( dados_plot) 
newlist = sorted(dados_plot, key=lambda k: k['qt'], reverse=True)     
cod = list (map(lambda x:x["cod"], newlist[1:10]))
qt = list (map(lambda x:x["qt"], newlist[1:10]))

bar (range(len(qt)),qt)
xticks(range(len(cod)), cod)
show()


