import pandas as pd
# import numpy as np
import streamlit as st
# import mysql.connector
# from evadellaapp import *
from evadella_mysql import *
import streamlit_authenticator as stauth



st.set_page_config(
    page_title="EvaDella App",
    page_icon="🧊",
    layout="wide",  
    initial_sidebar_state="collapsed"
)


# authenticator = stauth.Authenticate(credentials,
#         "dashborad", "abcdefg", cookie_expiry_days = 30)


# name, authentication_status, username = authenticator.login("login", "main")


# if authentication_status == False:
#     st.error("Please enter your correct username/password")

# if authentication_status:
st.title('Raw Data To Home Page')

# authenticator.logout("logout")

st.subheader('Total Orders Details')

# unShippedOrdersMonthCountDf1
ordersDf = pd.read_sql(ordersCount, mydb)

totalOrders = sum(ordersDf['No Of Orders'])

st.metric("Total No Of Orders", totalOrders)

st.dataframe(ordersDf)