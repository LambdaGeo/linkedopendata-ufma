import requests


url = 'http://localhost:5000/api/v01/curso/'
req_curso = requests.get(url)

cursos = req_curso.json()
total = len (cursos)




for ano in range(2014,2018):
    cod_monografia = 1
    for curso in cursos["data"]:
        #print (curso)
        url = 'http://localhost:5000/liveapi/v01/curso/'+curso["codigo"]+"/monografias/" + str(ano)
        #print (url)
        print (ano)
        req_monografias = requests.get(url)
        monografias = req_monografias.json()
        for monografia in monografias["data"]:
            monografia["codigo_curso"] = curso["codigo"]
            monografia["ano"] = str(ano)
            monografia["codigo"] = curso["codigo"]+"_"+str(ano)+str(cod_monografia)
            urldocente = "http://localhost:5000/api/v01/docente/?nome="+monografia['orientador']
            discentes = requests.get(urldocente).json()["data"]
            if (len (discentes) > 0):
                siape = discentes[0]["siape"]
                monografia["siape_orientador"] = siape
            print (monografia)
            
            post_url = "http://127.0.0.1:5000/api/v01/monografia/"+str(cod_monografia)
            response = requests.post(post_url, data=monografia)
            print (post_url)
            print (response)
            print (response.json())
            
            cod_monografia = cod_monografia + 1
