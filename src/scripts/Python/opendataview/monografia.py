import json, requests
from pylab import *


url = "http://dados.inova-campus.xyz/v01/educacional/monografias/?curso=85766&ano="


anos =[]
nd = []

for ano in range(2012,2016):
  
    r = requests.get(url+str(ano))
    dados = r.json()
    nd.append (int (dados["amount"]))
    anos.append (ano)
        
#print (total_docentes)        
bar (range(len(anos)),nd)
xticks(range(len(anos)), anos)
show()


