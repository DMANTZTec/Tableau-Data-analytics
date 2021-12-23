# from bokeh.plotting import figure, show
# from bokeh.resources import CDN
# from bokeh.embed import file_html
# from bokeh.models import ColumnDataSource
# from jinja2 import Template

# source = ColumnDataSource(data=dict(x=[1, 2, 3],
#                                     y=[3, 2, 1]),
#                           name='my-data-source')

# p = figure()
# p.line("x", "y", source=source)

# show(p)


class ChartProvider():
    
  def chartExample(self, id_):
    # Bokeh related code
    adapter = CustomJS(code="""
    const value = cb_data.response.number;
    const result = {label: [value]};
    return result;
    """)

    # create a new plot
    q = np.array([0,  0, 0, -1, -1,  1, 1]) - 2
    r = np.array([0, -1, 1,  0,  1, -1, 0])

    source = AjaxDataSource(data_url='http://localhost:9000/number',
                            polling_interval=300, adapter=adapter)

    p = figure(plot_height=HEIGHT, plot_width=WIDTH, background_fill_color="lightgrey",
               title="Number repesentation", toolbar_location=None, 
               match_aspect=True, x_range=[-6,2])
    p.grid.visible = False
    p.axis.visible = False
    p.hex_tile(q, r, size=1, fill_color=["firebrick"]*3 + ["navy"]*4,
               line_color="white", alpha=0.5)

    labels = LabelSet(x=-0.75, y=-0.75, text='label', level='glyph',
                      source=source, text_font_size="40pt")

    p.add_layout(labels)
    chart_item = json_item(p)
    return chart_item


