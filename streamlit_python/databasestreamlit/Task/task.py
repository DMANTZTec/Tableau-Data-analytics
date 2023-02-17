import pandas as pd
import numpy as np
import streamlit as st
from bokeh.plotting import figure
import mysql.connector
import matplotlib.pyplot as plt
from task_mysql import *
import plotly.express as px

st.set_page_config(
    page_title="Task Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

orderCountDf = pd.read_sql(ordersCount, mydb)

ordersLastMonthCountDf = pd.read_sql(ordersLastMonthCountDf, mydb)

unShippedordersWeekCountDf = pd.read_sql_query(unShippedordersWeekCount, mydb)

unShippedordersByDaysCountDf = pd.read_sql_query(unShippedordersByDaysCount, mydb)

ordersCountByCouponDf = pd.read_sql_query(ordersCountByCoupon, mydb)

unShippedordersMonthCountDf = pd.read_sql_query(unShippedordersMonthCount, mydb)

currentMonthOrdersDf = pd.read_sql(currentMonthOrders, mydb)


st.title("Sales Ecommerce App Dashboard")

with open('C:/Users/ADMIN_2/Python_Giridhar/App Analytics/Analytics/databasestreamlit/Task/style.css') as f:
    st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html = True)


col1, col2, col3, col4 = st.columns(4)


with col3:
    st.metric(st.text_input('Total Amount', sum('')),  value='')
with col2:
    st.metric("Profit","86%", "4%")
col1.metric("Number of sales", "25%", "-8%, 5%")
col4.metric("Number of sales", "25%", "-8%, 5%")


col2, col3 = st.columns(2)

with col2:
    st.subheader("Orders Count By Coupon Applied")

    st.table(ordersCountByCouponDf)

    # coupon_filter = st.selectbox("Select the status", pd.unique(ordersCountByCouponDf("coupon_applied")))

    optionSelect = st.selectbox("Coupon Applied", options= ordersCountByCouponDf['coupon_applied'])

    appliedCoupon = ordersCountByCouponDf.query("coupon_applied == @optionSelect")

    st.table(appliedCoupon)


with col3:
    st.subheader("Current Month Orders")
    def CurrentMonthOrders():
        currentMonthOrdersCount = currentMonthOrdersDf[['No Of Orders', 'Date', 'order_id']]
        return currentMonthOrdersCount

    currentMonthOrdersCountDF = CurrentMonthOrders()

    st.sidebar.header("Select Date Here:")

    orderedDates = st.sidebar.multiselect(
            "select:",
            options = currentMonthOrdersCountDF['Date'].unique()
    )
    filteredDf = currentMonthOrdersCountDF.query(
            # "OrderedDate == @ordereddate",
            "Date == @orderedDates",
            )
    st.table(filteredDf)


col4, col5 = st.columns(2)

with col4:
    st.subheader("Unshipped Orders Last Week")
    # unShippedordersWeekCountDf = unShippedordersWeekCountDf[['order_id', 'No Of Orders']

    st.bar_chart(unShippedordersWeekCountDf,  x = 'order_id', y = 'No Of Orders')
    
    
with col5:
    st.subheader("Unshipped Orders Last Days")

    st.table(unShippedordersByDaysCountDf)


col6, col7 = st.columns(2)


with col6:
    st.subheader('No Of Orders')

    def noOfOrders():
        noOfOrdersByMonth = (orderCountDf.groupby(['Year','Month Name'])['No Of Orders'].sum()).reset_index()
        return noOfOrdersByMonth

    noOfOrdersdf = noOfOrders()

    optionSelect = st.multiselect('select year', options=noOfOrdersdf['Year'])

    ordersByYearDf = noOfOrdersdf.query("Year == @optionSelect")

    st.table(ordersByYearDf)


with col7:
    st.subheader("Unshipped Orders Last Month")

    unShippedordersMonthCountDf = unShippedordersMonthCountDf[['order_id','No Of Orders' ]]

    st.bar_chart(unShippedordersMonthCountDf,  x='order_id', y='No Of Orders', use_container_width=True)
st.subheader("Last Month Orders Count")

fig = px.pie(ordersLastMonthCountDf, values='No Of Orders', names='Date')

st.plotly_chart(fig)