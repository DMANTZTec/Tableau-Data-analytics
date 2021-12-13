from bokeh.layouts import column
#from bokeh.models.sources import Index
import pandas as pd 
data = pd.read_csv("Data analytics with python\sample data analutics practise\webscraping_weather_report\extract.csv")
#from bokeh.models import ColumnarDataSourced
from bokeh.plotting import figure, show
from bokeh.palettes import Spectral5

# data.drop(data.columns[0], axis=1, inplace=True)
data.drop(data.columns[0], axis=1, inplace=True)
bf = print(data)
f = pd.DataFrame(bf)
print(f)
# gf = bf.groupby("Category").sum()
# print(gf)
