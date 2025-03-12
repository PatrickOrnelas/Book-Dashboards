import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv(r"./data/customer reviews.csv")
df_topic_100_books = pd.read_csv(r"./data/Top-100 Trending Books.csv")

price_min = df_topic_100_books['book price'].min()
price_max = df_topic_100_books['book price'].max()

max_price = st.sidebar.slider('Price Range :money_with_wings:', price_min, price_max, price_max)
df_books = df_topic_100_books[df_topic_100_books['book price'] <= max_price]

fig = px.bar(df_books['year of publication'].value_counts())
fig2 = px.histogram(df_books['book price'])

df_books

col1, col2 = st.columns(2)

col1.plotly_chart(fig)
col2.plotly_chart(fig2)

