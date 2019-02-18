# Vocabulários



| Nome | Prefix | Link | Objetivo |
| --- | --- | --- | --- |
| Teaching Core Vocabulary Specification  | ns | [http://linkedscience.org/teach/ns#](http://linkedscience.org/teach/ns) | Classificar os recursos, como professor, estudante, curso .. |
| Academic Institution Internal Structure Ontology (AIISO)  | aiiso | http://vocab.org/aiiso/schema# | Curso, departamento, |
| FOAF Vocabulary Specification 0.99 | Foaf | http://xmlns.com/foaf/spec/ | a dictionary of people-related terms that can be used in structured data |
| Dublin Core Metadata | dc |  [http://purl.org/dc/terms](http://purl.org/dc/terms/description) http://purl.org/dc/elements/1.1/  http://dublincore.org/documents/dces/ | |
| | bib | http://purl.org/ontology/bibo/ | |
| vCard Ontology - for describing People and Organizations | vcard | https://www.w3.org/TR/vcard-rdf/ | |



Entidades

DISCENTE

ID: http://lud.ufma.br/person/{matricula}

Class: ns:Student

| Propriedade | Vocabulário | Exemplo |
| --- | --- | --- |
| Nome | foaf:name | Lucas Jose Silva |
| Curso | foaf:member | http://lud.ufma.br/course/454353 |
|   |   |   |



CURSO

ID: http://lud.ufma.br/course/{id}

Class: aiiso:Course

| Propriedade | Vocabulário | Exemplo |
| --- | --- | --- |
| Nome | ns:courseTitle | Engenharia da Computação |
| Departamento | aiiso:part\_of | http://lud.ufma.br/course/454353 |
| Coordenador | aiiso:[responsibilityOf](http://purl.org/vocab/aiiso/schema#responsibilityOf) | http://lud.ufma.br/person/454353 |
| Area | dc:subject (nao ´e bom) |   |



DOCENTE

ID: [http://lud.ufma.br/person/{id](http://lud.ufma.br/professor/%7Bid)}

Class: ns:Teacher

| Propriedade | Vocabulário | Exemplo |
| --- | --- | --- |
| Nome | foaf:name | PAULO ROGERIO DE ALMEIDA RIBEIRO |
| Título | foaf:title | Doutor em Neurociência (Neuroinformática / Neurociência Computacional) pela Universidade de Tübingen (Alemanha) &amp; International Max Planck Research School for Cognitive and Systems Neuroscience (International Max Planck Research School for Neural Information Processing), mestre em Engenharia Mecatrônica pela Universidade do Minho (Portugal) e bacharel em Ciência da Computação pela Universidade Federal do Maranhão (UFMA) - Brasil. |
| Área de Interesse | foaf:interest | Experiência na área de Ciência da Computação com ênfase em Inteligência Computacional e Robótica, atuando principalmente nos seguintes temas: Robótica Móvel e Autônoma, Análise e Processamento de Dados e Sinais, Aprendizado de Máquina, Automação e Controle de Processos, Visão Computacional e Otimização. Também desenvolve projetos em Neurociência Computacional e Brain Computer-Interface (BCI). |
| Lattes | vcard:hasURL | http://lattes.cnpq.br/0035213619257246 |
| Telefone/Ramal | foaf:phone | 3272-9121 |
| Sala | ns:room | Null |
| E-mail | vcard:hasEmail | paulo.ribeiro@ecp.ufma.br |
| Departamento | foaf:member | DCCET |

&#39;



MONOGRAFIA

ID: [http://lud.ufma;br/publications/{id}](about:blank)

Class: bib:Thesis

| Propriedade | Vocabulário | Exemplo |
| --- | --- | --- |
| Título | dc:title | Desenvolvimento de uma Plataforma para Aprendizagem de Habilidade Motora Utilizando Processamento de Imagens |
| Autor(Discente) | dc:creator | http://lud.ufma.br/student/883793 |
| Orientador(Docente) | dc:contibutor | http://lud.ufma.br/professor/75655 |
| Curso | bib:issuer |   |
| Ano | bib:year |   |



CENTRO

ID: [http://lud.ufma.br/center/{id](http://lud.ufma.br/center/%7Bid)}

Class: aiiso:Center



| Propriedade | Vocabulário | Exemplo |
| --- | --- | --- |
| Nome | foaf:name |   |
| Diretor | aiiso:[responsibilityOf](http://purl.org/vocab/aiiso/schema#responsibilityOf) |   |
| Telefone | foaf:fone |   |



DEPARTAMENTO

ID: [http://lud.ufma.br/](http://lud.ufma.br/center/%7Bid)department/{id}

Class: aiiso:Department

| Propriedade | Vocabulário | Exemplo |
| --- | --- | --- |
| Nome | foaf:name | Engenharia da Computação |
| Chefe | aiiso:[responsibilityOf](http://purl.org/vocab/aiiso/schema#responsibilityOf) |   |
| Centro | aiiso:part\_of |   |


