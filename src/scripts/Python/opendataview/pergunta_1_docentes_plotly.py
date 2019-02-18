import json, requests
import plotly.plotly as py
from plotly.tools import FigureFactory as FF 


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
        

sorted_dados = sorted(dados_plot, key=lambda k: k['qt'], reverse=True)     


data_matrix = [["Nome","Quantidade de Docentes"]]
for v in sorted_dados[0:10]:
    data_matrix.append ([v["nome"],v["qt"]])
print (data_matrix)
table = FF.create_table(data_matrix)
py.iplot(table, filename='docentes_top_10_v2')
                         


