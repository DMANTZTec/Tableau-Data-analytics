import pandas
import justpy as jp
import matplotlib.pyplot as plt

data8 = pandas.read_excel("PROBLEM 1.xlsx")
data = pandas.read_excel("Book1 spend hours.xlsx")
data46 = pandas.read_excel("Spend Time.xlsx")

tasks = data.groupby(['Courses'])['Spend Hours'].mean()
print(tasks)

chart_def = """
{
    chart: {
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: ''
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: ''
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Course',
        colorByPoint: true,
        data: [{}]
    }]
}
"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Create a pie chart of for a developer on hours spend on each course.", 
            classes="text-h6 q-pr-md text-weight-bolder text-center")
    p1 = jp.QDiv(a=wp, text="These graphs represent course spende Hours analysis", classes= "text-h6 q-pr-md text-weight-medium text-center")
    hc = jp.HighCharts(a=wp, options=chart_def)
    # hc.options.xAxis.categories = tasks
    hc_data = [{"name":v1, "y":v2} for v1, v2 in zip(tasks.index, tasks)]
    hc.options.series[0].data = hc_data
 
    return wp
jp.justpy(app)