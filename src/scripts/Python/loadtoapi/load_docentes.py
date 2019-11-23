import requests


url = 'http://localhost:5000/api/v01/subunidade/'
r1 = requests.get(url)
subunidades = r1.json()["data"]

i = 0
for sub in subunidades[0:10]:
    i=i+1
    print (i, len(subunidades))
    codigo = sub['codigo']
    print (codigo)

    url = 'http://127.0.0.1:5000/liveapi/v01/subunidade/'+codigo+'/docente'
    print (url)

    docentes = []
    r = requests.get(url)
    dados = r.json()
    total = len (dados)

    for docente in dados:
        url = "http://127.0.0.1:5000/liveapi/v01/docente/"+docente["siape"]
        dados_docente = requests.get(url).json()
        dados_docente["codigo_subunidade"] = docente["codigo_subunidade"]
        print (dados_docente)
        post_url = "http://127.0.0.1:5000/api/v01/docente/"+docente["siape"]
        response = requests.post(post_url, data=dados_docente)
        print (post_url)
        print (response)
