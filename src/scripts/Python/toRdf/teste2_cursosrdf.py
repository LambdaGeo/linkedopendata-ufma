from rdflib.namespace import RDF, FOAF
from rdflib import URIRef, BNode, Literal
from rdflib import Graph
from rdflib import Namespace

import requests

g = Graph()
n = Namespace("http://linkedscience.org/teach/ns#")
g.bind("teach", n)


def dadoapi (url, att):
    dados = requests.get(url).json()['data']
    r = (dados != [] and dados[0][att]) or ""
    return r

url = 'https://dados-abertos-ufma.herokuapp.com/api/v01/cursos'

discentes = []
r = requests.get(url)
dados = r.json()['data']
total =  len (dados)
doc_cod = {}
for dado in dados:

    curso = URIRef("http://lud.ufma.br/course/"+dado["_id"])
    title = Literal(dado["nome"]) # passing a string
   
    g.add( (curso, RDF.type, n.Course) )
    g.add( (curso, n.courseTitle, title) )

    #depois pegar mais informações
    #s = dado["nome"] + ";" + dado["_id"] + ";" + dado["modalidade de curso"] + ";"
    #s = s + dado["area de conhecimento cnpq"] + ';"' + dado["descricao"] + '";'
    #s = s + dado["coordenacao do programa"] + ";"

    #url2 = "https://dados-abertos-ufma.herokuapp.com/api/v01/docentes?nome="+dado["coordenacao do programa"]

    #siape = doc_cod.get(dado["coordenacao do programa"]) or dadoapi(url2,"siape")
    #doc_cod[dado["coordenacao do programa"]] = siape



output = g.serialize(format='xml')
print (output)

file = open("saida.xml","w") 
file.write(output.decode())
file.close()


    