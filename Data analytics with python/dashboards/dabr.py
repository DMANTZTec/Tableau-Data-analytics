from flask import Flask, render_template

app = Flask(__name__)

@app.route('/plot/')
def plot():
    import pandas_bokeh
    from math import pi
    from bokeh.palettes import Category20c
    from bokeh.transform import cumsum
    import pandas as pd
    from bokeh.plotting import figure
    from bokeh.models import ColumnDataSource
    from bokeh.palettes import Spectral6
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN
    
    data = pd.read_excel("C:/Users/admin/Documents/Tableau Documentation/Data analytics with python/problems-2/PROBLEM 1.xlsx", 
            parse_dates=["START DATE"])
    g = pd.read_excel("Data analytics with python/dashboards/Nareshworksheet.xlsx", parse_dates=["Start Date"])
    t = pd.read_excel("Data analytics with python/dashboards/SwapnaTechWork.xlsx", parse_dates=["START DATE"])
    dt = pd.read_excel("Data analytics with python/dashboards/AmulyaTechwork.xlsx", parse_dates=["STARTDATE"])
    l = pd.read_excel("Data analytics with python/dashboards/Vamshi Techwork.xlsx", parse_dates=["START DATE"])


    n = g.groupby(["Subject", "Name"])["Module"].count()
    n1 = pd.Series(n).reset_index(name="Tasks")
    n2 = n1["Subject"].tolist()
    n3 = n1["Name"].tolist()
    n4 = n1["Tasks"].tolist()
    source = ColumnDataSource(data=dict(n2=n2, n4=n4, n3=n3, color=Spectral6))

    z = figure(x_range=n2, width=650, height=600, toolbar_location=None,
                tools="hover", tooltips="@n2, @n3: @n4 tasks", title="noOTasks by Subject,by Naresh")

    z.vbar(x="n2", top="n4", width=0.6, color="color",legend_field="n2", source=source)

    # show(z)

    colors = ["red","blue","pink","orange","purple","green","violet","yellow"]

    w = data.groupby(["TRAINEE"])["SPEND HOURS"].sum()
    w1 = dict(w)
    w2 = pd.Series(w1).reset_index(name= "value").rename(columns={"index": "Trainees"})
    w2['angle'] = w2['value']/w2['value'].sum() * 2*pi
    w2['color'] = colors   # Category20c[len(w1)] we can also use 
    w2

    j = figure(height=470, title="Pie Chart", toolbar_location=None,
            tools="hover", tooltips="@Trainees: @value Hrs", x_range=((-0.5, 1.0)))

    j.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='Trainees', source=w2)

    j.axis.axis_label = None
    j.axis.visible = False
    j.grid.grid_line_color = None

    # show(j)

    t["MONTH"] = t["START DATE"].dt.strftime('%m')
    t9= t[(t["MONTH"] == ("10"))]
    u = t9.groupby(["SUBJECT"])["ACTUALS"].count()
    u1 = u.index.tolist()
    u1
    source = ColumnDataSource(data=dict(u1=u1, u=u, color=Spectral6))

    v = figure(x_range=u1, width=430, height=340, toolbar_location=None,
                tools="hover", tooltips="@u1: @u Tasks", title="noOfTasks of Swapna in 10th month")

    v.vbar(x="u1", top="u", width=0.6, color="color",legend_field="u1", source=source)

    # show(v)

    df = dt.drop("Comments",1)
    df["MONTH"] = df["STARTDATE"].dt.strftime('%m')
    df1= df[(df["MONTH"] == ("10"))]
    e = df1.groupby(["SUBJECT"])["ACTUAL HOURS"].count()
    e1 = e.index.tolist()
    source = ColumnDataSource(data=dict(e1=e1, e=e, color=Spectral6))

    w = figure(x_range=e1, width=430, height=340, toolbar_location=None,
            tools="hover", tooltips="@e1: @e Tasks", title="noOfTasks of Amulya in 10th month")
    w.vbar(x="e1", top="e", width=0.6, color="color",legend_field="e1", source=source)

    # show(w)

    # l1 = l.groupby("SUBJECT")["ACTUAL HOURS"].sum()
    l11 = l.groupby("SUBJECT")["ACTUAL HOURS"].count()
    l12 = pd.Series(l11).reset_index(name="noOfTask")
    l13 = l12["SUBJECT"].tolist()
    l14 = l12["noOfTask"].tolist()
    l14

    source = ColumnDataSource(data=dict(l13=l13, l14=l14, color=Category20c[len(l13)]))

    f = figure(x_range=l13, width=550, height=630, toolbar_location=None,
                tools="hover", tooltips="@l13: @l14 Tasks", title="noOfTasks by courses by Vamshi")

    f.vbar(x="l13", top="l14", width=0.6, color="color",legend_field="l13", source=source)

    # show(f)

    script1, div1 = components(z)
    script2, div2 = components(v)
    script3, div3 = components(w)
    script4, div4 = components(f)
    script5, div5 = components(j)
    cdn_js = CDN.js_files[0]
    # cdn_css = CDN.css_files[0]
    return render_template("plot.html",
    script1 = script1, script2 = script2, script3 = script3, script4 = script4, script5 = script5,
    div1 = div1, div2 = div2, div3 = div3, div4 = div4, div5 = div5,
    # cdn_css = cdn_css,
    cdn_js = cdn_js)

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)