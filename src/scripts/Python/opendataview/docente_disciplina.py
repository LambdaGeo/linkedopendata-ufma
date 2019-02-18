
import json, requests


#1396

url = "https://script.google.com/macros/s/AKfycbyEfNvWitlEijpCSmidnguLxD-drkWbPD1Vq-WVX1gY_IdtDqw/exec?departamento=1396"
dados = requests.get(url).json()
q = "ALGORÍTMOS E ESTRUTURA DE DADOS (CT)"
l = []
for docente in dados:
    siape = docente["siape"]
    url2 = "https://script.google.com/macros/s/AKfycbxjYbgBYlXU6-wGKXTcb58p52VKEoFqYsIeZ7rp4YhM5GhIafcU/exec?siape="+siape
    dados2 = requests.get(url2).json()["data"]
    for disc in dados2:
        if disc["nome"] == q:
            l.append(docente)
            break
        
print (l)   
        





