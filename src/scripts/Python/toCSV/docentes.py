import requests
import matplotlib.pyplot as plt
url = 'https://dados-abertos-ufma.herokuapp.com/api/v01/docentes'

docentes = []
r = requests.get(url)
dados = r.json()['data']
arq = open('docentes.csv', 'w')
dep_cod = {}
total =  len (dados)
for docente in dados:
    s = docente["nome"] + ';"' + docente["areas_de_interesse"] + '";"' + docente["formacao_academica"] + '";'
    s = s + docente["departamento"] + ";" + docente["url_sigaa"] + ";" + docente["url_lattes"] + ";" + docente["siape"]
    url2 =  "https://dados-abertos-ufma.herokuapp.com/api/v01/subunidades?nome=" + docente["departamento"]
    codigo_dep = dep_cod.get(docente["departamento"])
    if codigo_dep == None:
        codigo_dep=""
        dados2 = requests.get(url2).json()['data']
        if dados2 != []:
            codigo_dep = dados2[0]['codigo']
            dep_cod[docente["departamento"]] = codigo_dep
    s = s + ";" + codigo_dep + "\n"
    print(total)
    total = total - 1
    docentes.append(s)
arq.writelines(docentes)
arq.close()

