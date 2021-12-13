from flask import Flask, render_template

app = Flask(__name__)

@app.route('/plot/')
def plot():
    import pandas as pd
    import pandas_bokeh
    from math import pi
    from bokeh.models import ColumnDataSource
    from bokeh.transform import cumsum
    from bokeh.palettes import Spectral6
    from bokeh.palettes import Category20c
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN


    df = pd.read_csv("Data analytics with python\sample data analutics practise\Output.csv")

    # print(df["Address"])
    s = df.groupby(["Address"])["Price"].sum()

    s1 = s.index.tolist()

    # s = df["Price"].tolist()
    # print(s1)

    source = ColumnDataSource(data=dict(s1=s1, s=s, color=Spectral6))

    d = figure(x_range = s1, width = 950, height = 370, title = "Chart on Price by address",
                tooltips = "@s1 : @s")

    d.vbar(x = "s1", top = "s", width=0.6, color="color", legend_field= "s1", source=source)

    d.xgrid.grid_line_color = None
    d.legend.orientation = "horizontal"
    d.legend.location = "top_center"

    # show(d)

    v = df.groupby(["Address", "Beds"])["Price"].sum()
    v1 = dict(v)
    v2 = pd.Series(v1).reset_index(name="value").rename(columns={"level_0": "Address", "level_1": "Beds"})
    v2['angle'] = v2['value']/v2['value'].sum() * 2*pi
    v2['color'] = Category20c[len(v1)]
    v2


    p = figure(height=350, title="Pie Chart", toolbar_location=None,
            tools="hover", tooltips="@Address, @Beds: @@value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='Address', source=v2)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    # show(p)

    script1, div1 = components(d)
    script2, div2 = components(p)
    cdn_js = CDN.js_files[0]
    # cdn_css = CDN.css_files[0]
    return render_template("plot.html",
    script1 = script1, script2 = script2,
    div1 = div1, div2 = div2,
    # cdn_css = cdn_css,
    cdn_js = cdn_js)
    
@app.route('/')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)