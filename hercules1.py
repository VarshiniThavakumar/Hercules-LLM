import os
from databricks import sql
import streamlit as st

host = os.getenv("dbc-1e8b3c46-6329.cloud.databricks.com")
http_path = os.getenv("/sql/1.0/warehouses/9400158928ed9893")
access_token = os.getenv("dapie406676db10514f02bc4ddc90265239d")

connection = sql.connect(
  server_hostname=host,
  http_path=http_path,
  access_token=access_token)

cursor = connection.cursor()

cursor.execute('SELECT * FROM RANGE(10)')
result = cursor.fetchall()

st.dataframe(result)
