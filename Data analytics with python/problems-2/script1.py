from flask import Flask, render_template

app = Flask(__name__)

@app.route('/plot/')
def plot():
    import pandas_bokeh
    import pandas
    from bokeh.plotting import figure
    data = pandas.read_excel("C:/Users/admin/Documents/Tableau Documentation/Data analytics with python/problems-2/PROBLEM 1.xlsx", parse_dates=["START DATE"])
    from bokeh.models import ColumnDataSource
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    s = data.groupby(["TRAINEE"]).sum()
    s1 = s.index.tolist()
    # s["names"] = s1   
    # s
    s1

    s = data.groupby(["TRAINEE"])["NO OF TASKS"].sum()
    # s["values"] = s["NO OF TASKS"]
    # s3=s["NO OF TASKS"].tolist()
    # s3
    s

    colors = ["red","blue","pink","orange","purple","green","violet","yellow"]

    source = ColumnDataSource(data=dict(s1=s1, s=s, color=colors))

    p = figure(x_range=s1, y_range=(0,9), width=1200, height=450, title="Chart On Trainee",
            toolbar_location=None, tools="")

    p.vbar(x="s1", top="s",width=0.6, color="color", legend_field="s1", source=source)

    p.xgrid.grid_line_color = None
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    # show(p)

    # r = data.groupby(["SUBJECT"])["NO OF TASKS"].sum()
    # r1 = r.index.tolist()
    # source = ColumnDataSource(data=dict(r1=r1, r=r, color=colors))

    # n = figure(x_range=r1, y_range=(0,15), width=1200, height=450, title="noOfTasks by subject",
    #         toolbar_location=None, tools="")

    # n.vbar(x="r1", top="r",width=0.6, color="color", legend_field="r1", source=source)

    # show(n)

    script1, div1 = components(p)
    # script2, div2 = components(n)
    cdn_js = CDN.js_files[0]
    # cdn_css = CDN.css_files[0]
    return render_template("plot.html",
    script1 = script1, #(script2 = script2, div2 = div2) 
    div1 = div1,
    # cdn_css = cdn_css,
    cdn_js = cdn_js)

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)