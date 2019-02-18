import json, requests
from pylab import *



url1 = "https://dados-abertos-ufma.herokuapp.com/api/v01/cursos"
r = requests.get(url1)
dados = r.json()["data"]
for d in dados:
   url2 = "http://dados.inova-campus.xyz/v01/educacional/monografias/?curso="+d["_id"]+"&ano="
   for ano in range (2016,2017):
       r2 = requests.get(url2+str(ano))
       dados2 = r2.json()["data"]
       print (dados2)
