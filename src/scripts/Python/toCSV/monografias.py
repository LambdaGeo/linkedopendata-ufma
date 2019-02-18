import requests
import matplotlib.pyplot as plt
#2017.1
#url = 'http://dadosabertos.ufma.br/api/action/datastore_search?resource_id=8e6ddc16-6045-4697-b1aa-39260037fa4b'

#url = "http://dadosabertos.ufma.br/api/action/datastore_search?resource_id=953249c3-22c3-4431-81f5-75e0892ae545"

url = "http://dadosabertos.ufma.br/api/action/datastore_search?resource_id=83fcac77-7ca6-418a-827a-bfc9942beb05"

linhas = []
r = requests.get(url)
dados = r.json()['result']['records']
arq = open('monografias_20172.csv', 'w')

curso_cod = {}
doc_cod = {}


def dadoapi (url, att):
    dados = requests.get(url).json()['data']
    r = (dados != [] and dados[0][att]) or ""
    return r

total =  len (dados)
for dado in dados:
    s = '"'+dado["titulo"]+'"' + ";" + dado["autor"] + ";" + dado["orientador"] + ";" + dado["tipo"]
    s = s + ";" + dado["data_defesa"] + ";" + dado["curso"]+ ";" + dado["ano"] 

    url2 = "https://dados-abertos-ufma.herokuapp.com/api/v01/discentes?nome="+dado["autor"]
    _dados_disc = requests.get(url2).json()['data']
    mat =  (_dados_disc != [] and _dados_disc[0]['matricula']) or ""
    # o aluno nao existe na base do heroku, por hora vamos esquecer esse cara
    if mat != "":
        url2 = "https://dados-abertos-ufma.herokuapp.com/api/v01/docentes?nome="+dado["orientador"]
        siape = doc_cod.get(dado["orientador"]) or dadoapi (url2, "siape")
        doc_cod[dado["orientador"]] = siape
        #print (siape)

        url3 = 'https://dados-abertos-ufma.herokuapp.com/api/v01/cursos?q="'+dado["curso"]+'"'
        id_curso = curso_cod.get(dado["curso"]) or dadoapi (url3, "_id") 
        curso_cod[dado["curso"]] = id_curso
        #print (id_curso)
        s = s + ";" + mat + ";" + siape + ";" + id_curso + "\n"
        linhas.append(s)
    
    print(total)
    total = total - 1
   
arq.writelines(linhas)
arq.close()





