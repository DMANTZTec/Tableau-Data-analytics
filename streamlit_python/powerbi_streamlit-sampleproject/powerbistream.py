import pandas as pd
import numpy as np
import streamlit as st
from bokeh.models import ColumnDataSource
from bokeh.palettes import Bright5
from bokeh.plotting import figure, output_file, show
import matplotlib.pyplot as plt
import plotly.express as px

cookiesDf = pd.read_excel('OneDrive-2022-11-30\Cookie Types.xlsx')

ordersDf = pd.read_excel('OneDrive-2022-11-30\Orders.xlsx')

customersDf = pd.read_excel('OneDrive-2022-11-30\Customers.xlsx')

ordersDf['Profit'] = (ordersDf['Revenue'] - ordersDf['Cost'])

st.header('Dashboard Of Powerbi - Streamlit')

st.write('This is the dashboard, which I done in powerbi tool. This dashboard explains the orders and customers (cost, profit, customer names) and aslo explains the interactions between cutomers & orders by products.')

# st.sidebar.header("Please Filter Here:")
# customersName = st.sidebar.multiselect(
#     "select"
#     options = customersDf['Name'].unique(),
#     default = ordersDf["CurrentStatus"].unique()    
# )

pd.DataFrame(ordersDf)

col1, col2,col3 = st.columns(3)

with col1:
    # st.header('Names with ID')
    st.metric(label="Total Profit", value="2.72 M")

with col2:
    filterDataFrame = (ordersDf.groupby('Customer ID').sum()).reset_index()
    profitMargine = (sum(filterDataFrame['Profit']/filterDataFrame['Revenue'])/5)*100
    st.metric(label="Profit Margine %", value=profitMargine)


# with col3:
    # st.metric(label="TotalUnitsSold", value=sum(unitsSoldOrdersCountDf['Units Sold']))

col4, col5 = st.columns([2, 3])

with col4:

    st.subheader('TotalUnitsSold & OrdersCount')

    def UnitsSoldOrdersCount():
        global customerOrdersdf
        customersNameDf = customersDf[['Customer ID', 'Name']]
        filterDataFrame = (ordersDf.groupby('Customer ID').sum()).reset_index()
        customerOrdersdf = pd.merge(customersNameDf, filterDataFrame, on="Customer ID")
        totalCookiesSoldDf = customerOrdersdf[['Customer ID','Name', 'Units Sold']]
        ordersCountdf = (ordersDf.groupby('Customer ID')['Order ID'].count()).reset_index()
        ordersCountdf.rename(columns={'Order ID': 'Orders Count'}, inplace=True)
        ordersCountUnitsSoldDf = pd.merge(totalCookiesSoldDf, ordersCountdf, on="Customer ID")

        return ordersCountUnitsSoldDf
    unitsSoldOrdersCountDf = UnitsSoldOrdersCount()
    

    st.sidebar.header("Please Filter Here:")

    customersName = st.sidebar.multiselect(
            "select:",
            options = unitsSoldOrdersCountDf['Name'].unique(),
            default = unitsSoldOrdersCountDf['Name'].unique()
    )

    # unitsSoldOrdersCountDf

    filteredDf = unitsSoldOrdersCountDf.query(
            # "OrderedDate == @ordereddate",
            "Name == @customersName",
            )

    filteredDf

with col5:


    def ProfitByProduct():
        # st.subheader('Sum Of Profit By Products')
        sumOfProfitDf = (ordersDf.groupby('Product')['Units Sold', 'Revenue', 'Cost', 'Profit'].sum()).reset_index() 
        sumOfProfitDf["Profit"] = ((sumOfProfitDf['Revenue']) - (sumOfProfitDf['Cost']))
        dataFrame = sumOfProfitDf[['Product', 'Profit']]
        profitByProduct = pd.DataFrame(dataFrame)
        return profitByProduct
        
    def ProfitByProduct2(listOfProducts):
        pd.DataFrame(ordersDf)
        sumOfProfitDf = (ordersDf.groupby('Product')['Units Sold', 'Revenue', 'Cost', 'Profit']).sum().reset_index() 
        sumOfProfitDf1 = pd.DataFrame(sumOfProfitDf)
        sumOfProfitDf1 = sumOfProfitDf1.loc[sumOfProfitDf1['Product'].isin(listOfProducts)]
        sumOfProfitDf1["Profit"] = ((sumOfProfitDf1['Revenue']) - (sumOfProfitDf1['Cost']))
        dataFrame = sumOfProfitDf1[['Product', 'Profit']]
        profitByProduct = pd.DataFrame(dataFrame)
        return profitByProduct

    st.subheader('Sum Of Profit By Products')
    sumOfProfitByProduct = ProfitByProduct()

    # st.bar_chart(sumOfProfitByProduct, x='Product', y='Profit', width=500)
    optionsSelect = st.multiselect(
    'select the product',
    options = sumOfProfitByProduct['Product']
    )

    if len(optionsSelect) > 0:
        df1 = ProfitByProduct2(optionsSelect)
        st.line_chart(df1, x= 'Product', y= 'Profit')


with col3:
    st.metric(label="TotalUnitsSold", value=sum(unitsSoldOrdersCountDf['Units Sold']))

def SumOfCostByName():
    st.subheader('Sum Of Cost By Name')

    sumOfCostByNameDf = customerOrdersdf[['Name', 'Cost']]

    fig = px.pie(sumOfCostByNameDf, values='Cost', names='Name')

    st.plotly_chart(fig)

SumOfCostByName()

def SumOfProfitByDayOfWeek():
    st.subheader('Sum Of Profit By Day of Week')

    ordersDf['Day of Week'] = ordersDf['Date'].dt.day_of_week

    sumOfProfitByDayOfWeek = (ordersDf.groupby(['Day of Week'])['Profit'].sum()).reset_index()

    st.bar_chart(sumOfProfitByDayOfWeek, x='Day of Week', y='Profit')

SumOfProfitByDayOfWeek()

