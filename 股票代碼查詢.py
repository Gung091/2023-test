# -*- coding: utf-8 -*-
"""股票代碼查詢.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14hZVMzkBEsUJpdWWUmzepZIfzhUJ-vHy
"""


import streamlit as st
import pandas as pd

df=pd.read_csv("TWSE_TW-1.csv")
df.fillna('', inplace=True)

st.title("TWSE Stock Search, 台灣股票代號查詢")

search_term = st.text_input("Enter search term, 輸入查詢資料:")
search_by = st.selectbox("Search by column:", options=['Symbol 公司代碼', 'Name 公司名稱'])

if search_term:
    if search_by == 'Symbol 公司代碼':
        result = df[df['Symbol'].str.contains(search_term)]
    elif search_by == 'Name 公司名稱':
        result = df[df['Name'].str.contains(search_term)]
    else:
        result = pd.DataFrame()
    st.write('Search ',search_term,' by ', search_by )   
    st.write(result)
