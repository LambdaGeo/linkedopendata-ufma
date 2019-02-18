import json, requests
from pylab import *


url = "http://dados.inova-campus.xyz/v01/educacional/monografias/?curso=85829&ano="


anos =[]
nd = []

for ano in range(2011,2017):
  
    r = requests.get(url+str(ano))
    dados = r.json()["data"]
    for m in dados:
        print (m["titulo"].upper())
        
#print (total_docentes)        
#bar (range(len(anos)),nd)
#xticks(range(len(anos)), anos)
#show()


