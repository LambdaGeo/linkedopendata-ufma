import requests
import matplotlib.pyplot as plt


def dadoapi (url, att):
    dados = requests.get(url).json()['data']
    r = (dados != [] and dados[0][att]) or ""
    return r

url = 'https://dados-abertos-ufma.herokuapp.com/api/v01/unidades'

linhas = []
r = requests.get(url)
dados = r.json()['data']
arq = open('unidades.csv', 'w')
total =  len (dados)
doc_cod = {}
for dado in dados:
    s = dado["nome"] + ";" + dado["sigla"] + ";" + dado["diretor"] + ";"
    s = s + (dado["siape_diretor"] or "") + ';"' + dado["apresentacao"] + '";'
    #print (dado)
    url_unidade = dado["url_sigaa"]
    
    id_unidade = url_unidade[url_unidade.find("id=")+3:]
 
    s = s + id_unidade + ";" + url_unidade  + "\n"
    print(total)
    total = total - 1
    linhas.append(s)
    
arq.writelines(linhas)
arq.close()




