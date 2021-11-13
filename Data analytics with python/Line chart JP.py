import pandas
import justpy as jp
import matplotlib.pyplot as plt

data8 = pandas.read_excel("PROBLEM 1.xlsx")
data = pandas.read_excel("Book1 spend hours.xlsx")
data46 = pandas.read_excel("Spend Time.xlsx")


chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: ''
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Start Date'
        },
        labels: {
            format: '{value} '
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 .'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Spend Time'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} day: {point.y} hrs'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Spend Time'
    }]
}
"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Line chart on how a developer spent time on a particular course over a period of month.", 
            classes="text-h6 q-pr-md text-weight-bolder text-center")
    p1 = jp.QDiv(a=wp, text="These graphs represent course spended time analysis", classes= "text-h6 q-pr-md text-weight-medium text-center")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(data46['Start Date'])
    hc.options.series[0].data = list(data46['Spend Time']) 
 
    return wp
jp.justpy(app)