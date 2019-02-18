import plotly.plotly as py
from plotly.tools import FigureFactory as FF 



data_matrix = [['Country', 'Year', 'Population'],
               ['United States', 2000, 282200000],
               ['Canada', 2000, 27790000],
               ['United States', 2005, 295500000],
               ['Canada', 2005, 32310000],
               ['United States', 2010, 309000000],
               ['Canada', 2010, 34000000]]

table = FF.create_table(data_matrix)
py.iplot(table, filename='simple_table')
