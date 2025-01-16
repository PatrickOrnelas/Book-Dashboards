import streamlit as st
import pandas as pd

df_reviews = pd.read_csv("dados/customer reviews.csv")
df_topic_100_books = pd.read_csv("dados/Top-100 Trending Books.csv")

books = df_topic_100_books['book title'].unique()
book = st.sidebar.selectbox("Books", books)

df_book = df_topic_100_books[df_topic_100_books['book title'] == book]
df_reviews_f = df_reviews[df_reviews['book name'] == book]

book_title = df_book['book title'].iloc[0]
book_genre = df_book['genre'].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book['rating'].iloc[0]
book_year = df_book['year of publication'].iloc[0]

st.title(book_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)
col1.metric("Price :money_with_wings:", book_price)
col2.metric(f"Rating :star:", book_rating)
col3.metric("Year of Publication :calendar:", book_year)

st.divider()
st.subheader("Reviews :speech_balloon:")

for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"{row[2]}")
    message.write(f"{row[5]}")
    st.divider()