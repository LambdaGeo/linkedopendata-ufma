import json, requests
from pylab import *


url = "http://dados.inova-campus.xyz/v01/organizacional/departamentos/"

r = requests.get(url)

dados = r.json()

cod =[]
nd = []

total_docentes = 0
for v in dados:
  
    url2 = "http://dados.inova-campus.xyz/v01/pessoas/docentes/?departamento="+v['cod']   
    r2 = requests.get(url2)
    dados2 = r2.json()
    n = len(dados2)
    if n > 0:
        total_docentes = total_docentes + n
        nd.append(n)
        cod.append(v['cod'])
        print(v['cod'],",", v['nome'], ",", n ) 
        
print (total_docentes)        
bar (range(len(cod)),nd)
xticks(range(len(cod)), cod)
show()


