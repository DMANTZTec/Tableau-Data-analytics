import pandas as pd
import streamlit as st
import mysql.connector
from mysql.connector import connection
from sqlalchemy import create_engine
import pandas as pd


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


cursor = mydb.cursor()
cursor.execute("SELECT * FROM ecomm.product_sku")

dataFrame = cursor.fetchall()
 
# for x in dataFrame:
  

print(pd.DataFrame(dataFrame))

# productSkuDf = pd.read_sql("SELECT * FROM product_sku", cursor)
# print(productSkuDf)

# print(cursor)
