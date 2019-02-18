library(jsonlite)
library(httr)

url <- "http://dados.inova-campus.xyz/v01/pessoas/docentes/?departamento=COORDENACAO%20DO%20CURSO%20DE%20ENGENHARIA%20DA%20COMPUTACAO/DCCET"
req <- GET (url)
json <- content(req, as = "text")
data <- fromJSON(json)$data

x <- vector ("numeric", length = dim(data[1])[1])

for (i in 1:dim(data[1])[1]) {
  siape <- data[i,3]
  url2 = paste("http://dados-abertos-ufma.herokuapp.com/api/v01/turmas?siape_docente=", siape, sep="")
  req1 <- GET (url2)
  json1 <- content(req1, as = "text")
  disciplinas <- fromJSON(json1)$data
  somach =0
  tam = dim(disciplinas[5])
  corrente <- disciplinas[disciplinas$semestre == "2016.2",]
  if (dim(corrente[7]) > 0) {
    somach <- sum(sapply (corrente[7], as.numeric))
    x[i] = somach / 15
  } 
}

plot (factor (x))

