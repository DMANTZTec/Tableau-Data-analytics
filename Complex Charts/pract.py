# from bokeh.models import FactorRange
# from bokeh.plotting import figure, show
# # import pdb
# # pdb.set_trace()
# factors = [
#     ("python", "naresh"), ("python", "giri"), ("python", "mamatha"),
#     ("Q2", "apr"), ("Q2", "may"), ("Q2", "jun"),
#     ("Q3", "jul"), ("Q3", "aug"), ("Q3", "sep"),
#     ("Q4", "oct"), ("Q4", "nov"), ("Q4", "dec"),
# ]

# p = figure(x_range=FactorRange(*factors), height=400,
#            toolbar_location=None, tools="")

# x = [ 10, 12, 16, 9, 10, 8, 12, 13, 14, 14, 12, 16 ]
# p.vbar(x=factors, top=x, width=0.9, alpha=0.5)

# p.line(x=["python", "Q2", "Q3", "Q4"], y=[12, 9, 13, 14], color="red", line_width=2)

# p.y_range.start = 0
# p.x_range.range_padding = 0.1
# p.xaxis.major_label_orientation = 1
# p.xgrid.grid_line_color = None

# show(p)


from bokeh.plotting import figure, output_file, show
from bokeh.models.ranges import Range1d
import numpy


output_file("line_bar.html")

p = figure(plot_width=400, plot_height=400)

# setting bar values
h = numpy.array([2, 8, 5, 10, 7])

# Correcting the bottom position of the bars to be on the 0 line.
adj_h = h/2

# add bar renderer
p.rect(x=[1, 2, 3, 4, 5], y=adj_h, width=0.4, height=h, color="#CAB2D6")

# add a line renderer
p.line([1, 2, 3, 4, 5], [6, 7, 6, 4, 5], line_width=2)

# Setting the y  axis range   
p.y_range = Range1d(0, 12)

p.title = "Line and Bar"

show(p)

