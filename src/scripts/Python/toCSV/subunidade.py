import requests
import matplotlib.pyplot as plt


def dadoapi (url, att):
    dados = requests.get(url).json()['data']
    r = (dados != [] and dados[0][att]) or ""
    return r

url = 'https://dados-abertos-ufma.herokuapp.com/api/v01/subunidades'

linhas = []
r = requests.get(url)
dados = r.json()['data']
arq = open('subunidades.csv', 'w')
total =  len (dados)
doc_cod = {}
for dado in dados:
    s = dado["nome"] + ";" + dado["codigo"] + ";" + dado["localidade"] + "\n"

    print(total)
    total = total - 1
    linhas.append(s)
    
arq.writelines(linhas)
arq.close()



