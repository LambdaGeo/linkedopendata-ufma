# ludufma


A linguagem SPARQL permite realizar buscas complexas com apenas uma única requisição, diferentemente de uma arquitetura orientada a recurso, como o REST. Nessa arquitetura cada entidade representa um recurso e tem o seu endpoint proprio. Considere então a seguinte consulta:

Dado uma base de dados de monografia, me retorne o título, nome do discente, nome do orientador, curriculo lattes do orientador e o nome do curso. De todos os orientadores que tem como área de interesse "História".
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX ns: <http://linkedscience.org/teach/ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?titulo ?nome_discente ?nome_orientador ?interesse_orientador ?nome_curso
WHERE
{
?m dc:title ?titulo.
?m dc:creator ?url_discente.
?m dc:contributor ?url_docente.
?url_discente foaf:name ?nome_discente.
?url_discente foaf:member ?url_curso.
?url_curso ns:courseTitle ?nome_curso.
?url_docente foaf:name ?nome_orientador.
?url_docente foaf:interest ?interesse_orientador.
FILTER regex(?interesse_orientador, "História")

}
limit 20
```

vagrant

sudo pacman -S linux46-virtualbox-host-modules
sudo /sbin/rcvboxdrv setup
