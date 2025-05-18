import streamlit as st
from langchain_config import llm_chain

st.title('A Tool For Analyzing Equity Research News 📜')
st.write('Enter Your Query To Get The Latest News Articles Summarized.')
query = st.text_input('PLEASE ENTER YOUR QUERY 👇')
if st.button('Get News 📋'):
    if query:
         response = llm_chain.run({'query': query})
         st.write('### Summary:')
         st.write(response)
    else:
        st.write('PLEASE ENTER YOUR QUERY FIRST 👆')

