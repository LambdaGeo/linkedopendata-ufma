import json, requests
import plotly.plotly as py
from plotly.tools import FigureFactory as FF 


areas= ["Ciências Exatas e da Terra","Ciências Biológicas","Engenharias","Ciências da Saúde","Lingüística, Letras e Artes","Ciências Agrárias","Ciências Sociais Aplicadas","Ciências Humanas"]
dados_plot = []
#"_id":"15458361"
#https://dados-abertos-ufma.herokuapp.com/api/v01/discentes?curso_id=15458361
for area in areas:
  
    url = "https://dados-abertos-ufma.herokuapp.com/api/v01/cursos?area%20de%20conhecimento%20cnpq="+area   
    ob = requests.get(url).json()
    qt_cursos = ob["amount"]
    cursos = ob["data"]
    qt_discentes = 0
    for curso in cursos:
        url2 = "https://dados-abertos-ufma.herokuapp.com/api/v01/discentes?curso_id="+curso["_id"]
        ob = requests.get(url2).json()
        qt_discentes = qt_discentes + ob["amount"]
    print (qt_cursos,qt_discentes)
    dados_plot.append ({"area": area, "qt_curso":qt_cursos, "qt_discentes":qt_discentes })
        
data_matrix = [["Área de Conhecimento","Num. Curso","Num. Discentes"]]
for v in dados_plot:
    data_matrix.append ([v["area"],v["qt_curso"],v["qt_discentes"]])
print (data_matrix)
table = FF.create_table(data_matrix)
py.iplot(table, filename='discentes_area_completo')

                         


