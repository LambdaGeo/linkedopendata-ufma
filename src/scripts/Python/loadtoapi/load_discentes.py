import requests


url = 'http://localhost:5000/api/v01/curso/'
req_curso = requests.get(url)

cursos = req_curso.json()["data"]
total = len (cursos) # 290
i = 1
for curso in cursos:
    print (i, total)
    url = 'http://localhost:5000/liveapi/v01/curso/'+curso["codigo"]+"/discentes"
    print (url)
    req_discentes = requests.get(url)
    discentes = req_discentes.json()
    #print (discentes)
    for discente in discentes["data"]:
        post_url = "http://127.0.0.1:5000/api/v01/discente/"+discente["matricula"]
        response = requests.post(post_url, data=discente)
        print (post_url)
        print (response)
        print (response.json())