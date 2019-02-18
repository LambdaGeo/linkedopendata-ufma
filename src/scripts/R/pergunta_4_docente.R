library(jsonlite)
library(httr)


url = paste("https://dados-abertos-ufma.herokuapp.com/api/v01/turmas?siape_docente=2019434")
req <- GET (url)
json <- content(req, as = "text")
d <- fromJSON(json)
disciplinas <- d$data
dados <- transform (disciplinas, ch = as.numeric (ch))
  ag = aggregate(ch ~ semestre, data = dados, FUN= sum)
barplot(ag$ch, type="l", col="blue", 
axes=FALSE, ann=FALSE,ylim = c(0, 200))
axis(2, las=1, at=seq(0,200 , 30))
axis(1, at=1:length(ag$semestre), lab=ag$semestre)



