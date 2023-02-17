import pandas as pd
import numpy as np
import streamlit as st
import mysql.connector
from mysql.connector import connection
from sqlalchemy import create_engine


st.sidebar.header("Products")


col1, col2 = st.columns(2)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "swapna2021",
    database = "ecomm"
)

# engine = create_engine("mssql+pyodbc://root:@127.0.0.1", pool_recycle=3600)
# dbConnection = engine.connect()
# frame = pd.read_sql("SELECT * FROM product_sku", dbConnection)
# pd.set_option('display.expand_frame_repr', False)

with col1:

    st.header('productSku_Df')

    queryproductSkuDf = "SELECT * FROM ecomm.product_sku"

    productSkuDf = pd.read_sql(queryproductSkuDf, mydb)

    productSkuCostDf = (productSkuDf.groupby(['product_sku_id', 'product_sku_cd', 'product_id'])['price'].sum()).reset_index()

    productDf = pd.read_sql_query("SELECT * FROM ecomm.product", mydb)

    st.dataframe(productSkuCostDf)


with col2:

    st.header('orders_Df')

    ordersDf = pd.read_sql_query("SELECT * FROM ecomm.orders", mydb)

    ordersToatlAmountDf = (ordersDf.groupby(['order_id', 'customer_id', 'status', 'order_submit_dt_tm'])['total_amount'].sum()).reset_index()
    
    st.dataframe(ordersToatlAmountDf)


col3, col4 = st.columns(2)

with col3:

    st.header('products_Df')

    productDf = pd.read_sql_query("SELECT * FROM ecomm.product", mydb)

    st.dataframe(productDf)


with col4:

    st.header('ordersStatus_Df')

    def OrderStatus():

        # global filteredOrdersDf

        orderStatusDf = pd.read_sql_query("SELECT * FROM ecomm.order_status", mydb)

        filterOrdersDf = orderStatusDf[['order_id', 'status_cd', 'estimated_time']]
        
        filterOrdersDf['ordered_date'] = filterOrdersDf['estimated_time'].dt.date

        ordersCountDf = (filterOrdersDf.groupby(['ordered_date', 'status_cd'])['order_id'].count()).reset_index()

        countOfOrdersStatus = ordersCountDf.pivot_table(index = 'status_cd', columns='ordered_date', values='ordered_date', aggfunc='count')

        countOfOrdersStatusDf = ((countOfOrdersStatus.replace(np.nan, 0)).astype(int)).iloc[:, ::-1]

        sumoforders = countOfOrdersStatusDf.iloc[:, 3:].sum(axis=1)

        df0 = countOfOrdersStatusDf.drop(countOfOrdersStatusDf.iloc[:, 3:], axis=1)

        df0['Previous_orders_sum'] = sumoforders

        df3 = pd.DataFrame(df0)

        st.dataframe(df3)

    OrderStatus()

def OrdersCount():
    st.header('ordersCount_Df')

    orderStatusDf = pd.read_sql_query('select * from ecomm.order_status', mydb)

    filterOrdersDf = orderStatusDf[['order_id', 'status_cd', 'estimated_time']]

    filterOrderCount = filterOrdersDf.dropna(subset = ['estimated_time'])

    filterOrderCount['ordered_date'] = filterOrderCount['estimated_time'].dt.date

    ordersCountDf = (filterOrderCount.groupby(['ordered_date', 'status_cd'])['order_id'].count()).reset_index()

    ordersCountDf.rename(columns= {'order_id': 'order_count'}, inplace= True)

    st.dataframe(ordersCountDf)

OrdersCount()   

orderStatusDf = pd.read_sql_query('select * from ecomm.order_status', mydb)

st.subheader('2020 year Orders Count By Month')

def OrderStatusDf():

    global filterOrdersdf

    orderStatusDf = pd.read_sql_query("SELECT * FROM ecomm.order_status", mydb)

    filterOrders = orderStatusDf[['order_id', 'status_cd', 'estimated_time']]

    filterOrdersdf = filterOrders.dropna(subset = ['estimated_time'])
    
    # filteredOrdersDf['ordered_date'] = filteredOrdersDf['estimated_time'].dt.date  

    filterOrdersdf['years'] = (filterOrdersdf['estimated_time'].dt.year)
    filterOrdersdf['month'] = (filterOrdersdf['estimated_time'].dt.month)

    monthDf = filterOrdersdf[(filterOrdersdf['years']== 2020)]

    monthOrdersCount = (monthDf.groupby(['status_cd', 'estimated_time'])['order_id'].count()).reset_index()

    monthOrdersCount['date'] = monthOrdersCount['estimated_time'].dt.date

    monthOrdersCountDf = monthOrdersCount.pivot_table(index='status_cd', columns='date', values='order_id', aggfunc='count')

    monthOrdersCountByYearDf = (monthOrdersCountDf.replace(np.nan, 0).astype(int))

    monthOrdersCountByYearDf

    st.bar_chart(monthOrdersCountByYearDf, x=['date'])

OrderStatusDf()

def OrderStatusByYearDf():

    global filterOrdersdf

    orderStatusDf = pd.read_sql_query("SELECT * FROM ecomm.order_status", mydb)

    filterOrdersdf = orderStatusDf[['order_id', 'status_cd', 'estimated_time']]

    filterOrdersdf = filterOrdersdf.dropna(subset = ['estimated_time'])
    
    # filteredOrdersDf['ordered_date'] = filteredOrdersDf['estimated_time'].dt.date  

    filterOrdersdf['years'] = (filterOrdersdf['estimated_time'].dt.year)

    filterOrdersdf['month'] = (filterOrdersdf['estimated_time'].dt.month)

    # st.date_input()

    # return filterOrdersdf
    st.dataframe(filterOrdersdf)

# OrderStatusByYearDf()

def OrderStatusByYearDf1(yearslist):

    orderStatusDf = pd.read_sql_query("SELECT * FROM ecomm.order_status", mydb)

    filterOrdersdf = orderStatusDf[['order_id', 'status_cd', 'estimated_time']]

    filterOrdersdf = filterOrdersdf.dropna(subset = ['estimated_time'])
    
    # filteredOrdersDf['ordered_date'] = filteredOrdersDf['estimated_time'].dt.date

    filterOrdersdf['years'] = (filterOrdersdf['estimated_time'].dt.year)

    filterOrdersdf = filterOrdersdf.loc[filterOrdersdf['years'].isin(yearslist)]

    filterOrdersdf['month'] = (filterOrdersdf['estimated_time'].dt.month)
    
    yearsListDf = (filterOrdersdf.groupby(['years'])['month'].count()).reset_index()

    return filterOrdersdf


filterOrderCountDf = OrderStatusByYearDf()

# optionSelect = st.selectbox('select the year', filterOrderCountDf['years'])

# if len(optionSelect) > 0:
#     monthOrdersCountByYear = OrderStatusByYearDf1(optionSelect)
#     st.dataframe(monthOrdersCountByYear)



# option = st.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone'))

# st.write('You selected:', option)