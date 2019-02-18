import requests
import matplotlib.pyplot as plt


def dadoapi (url, att):
    dados = requests.get(url).json()['data']
    r = (dados != [] and dados[0][att]) or ""
    return r

url = 'https://dados-abertos-ufma.herokuapp.com/api/v01/cursos'

discentes = []
r = requests.get(url)
dados = r.json()['data']
arq = open('cursos.csv', 'w')
total =  len (dados)
doc_cod = {}
for dado in dados:
    s = dado["nome"] + ";" + dado["_id"] + ";" + dado["modalidade de curso"] + ";"
    s = s + dado["area de conhecimento cnpq"] + ';"' + dado["descricao"] + '";'
    s = s + dado["coordenacao do programa"] + ";"

    url2 = "https://dados-abertos-ufma.herokuapp.com/api/v01/docentes?nome="+dado["coordenacao do programa"]

    siape = doc_cod.get(dado["coordenacao do programa"]) or dadoapi(url2,"siape")
    doc_cod[dado["coordenacao do programa"]] = siape

    
    s = s + siape + "\n"
    print(total)
    total = total - 1
    discentes.append(s)
arq.writelines(discentes)
arq.close()



