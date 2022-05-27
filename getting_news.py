import streamlit as st
import requests
import api

def get_news():
    query_input = st.text_input("👉 Enter the automobile keywords to get news.")
    btn = st.button('Enter')

    if btn:
        url = f"https://newsapi.org/v2/everything?q={query_input}&apiKey=229d0e7cfd7748979970f4a2cf645f6b"
        r = requests.get(url)
        r = r.json()
        articles = r['articles']
        for article in articles:
            st.markdown(f"<h3 style='background-color:#FFC0CB;'> {article['title']}</h3>",unsafe_allow_html=True)
            st.markdown(f"<h4> Published at: {article['publishedAt']}</h4>",unsafe_allow_html=True)
            if article['author']:
                st.write("Author : "+ article['author'])
            st.write("Source : " + article['source']['name'])
            st.write(article['description'])
            st.image(article['urlToImage'])
