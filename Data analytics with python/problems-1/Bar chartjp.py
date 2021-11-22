import pandas
import justpy as jp
import matplotlib.pyplot as plt

data8 = pandas.read_excel("PROBLEM 1.xlsx")
data = pandas.read_excel("Book1 spend hours.xlsx")
data46 = pandas.read_excel("Spend Time.xlsx")

tasks = data8.groupby(['TRAINEE'])['SUBJECT'].count()
print(tasks)

chart_def = """chart('container',
{
    chart: {
        type: 'column'
    },
    title: {
        text: ''
    },
    xAxis: {
        categories: []
    },
    yAxis: {
        min: 0,
        title: {
            text: 'No of tasks'
        },
        stackLabels: {
            enabled: true,
            style: {
                fontWeight: 'bold',
                color: ( // theme
                    Highcharts.defaultOptions.title.style &&
                    Highcharts.defaultOptions.title.style.color
                ) || 'gray'
            }
        }
    },
    legend: {
        align: 'right',
        x: -30,
        verticalAlign: 'top',
        y: 25,
        floating: true,
        backgroundColor:
            Highcharts.defaultOptions.legend.backgroundColor || 'white',
        borderColor: '#CCC',
        borderWidth: 1,
        shadow: false
    },
    tooltip: {
        headerFormat: '<b>{point.x}</b><br/>',
        pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
    },
    plotOptions: {
        column: {
            stacking: 'normal',
            dataLabels: {
                enabled: true
            }
        }
    },
    series: [{

    }]
});
"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Create a bar chart with number of tasks that are completed by each trainee in last week.",
        classes="text-h6 q-pr-md text-weight-bolder text-center")
    p1 = jp.QDiv(a=wp, text="These graphs represent course No of tasks analysis", classes= "text-h6 q-pr-md text-weight-medium text-center")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(tasks.index)
    hc.options.series[0].data = list(tasks)

    return wp
jp.justpy(app)