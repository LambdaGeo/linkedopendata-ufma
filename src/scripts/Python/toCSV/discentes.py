import requests
import matplotlib.pyplot as plt
url = 'https://dados-abertos-ufma.herokuapp.com/api/v01/discentes'

discentes = []
r = requests.get(url)
dados = r.json()['data']
arq = open('discentes_total.csv', 'w')
dep_cod = {}
total =  len (dados)
for docente in dados:
    s = docente["nome"] + ";" + docente["matricula"] + ";" + docente["curso_id"] + "\n"
    print(total)
    total = total - 1
    discentes.append(s)
arq.writelines(discentes)
arq.close()

