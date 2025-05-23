# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cHgw0KRSd2TmDRghkUc89slROGj5Cejx
"""

!pip install streamlit

#Import libraries
import streamlit as st
import requests

#Display the Kenyan flag
st.image("kenyan_flag.jpg", width=200)
st.title("The Constitution of Kenya")
st.subheader("Search the Constitution of Kenya PDF using Groq and Langchain")
st.write("This bot allows you to search the Constitution of Kenya PDF using Groq and Langchain. You can ask questions about the content of the PDF and get answers in real-time.")
st.write("Please enter your question below 🔎:")
question = st.text_input("Question", "")

if st.button("Ask") and query:
    with st.spinner("Looking up the Constitution..."):
        try:
            response = requests.post("http://localhost:8000/ask", json={"query": query})
            data = response.json()

            st.markdown("### 🧠 Answer")
            st.success(data.get("answer", "No answer found."))

            st.markdown("---")
            st.markdown("### 📚 Sources")
            sources = data.get("sources", [])
            if sources:
                for i, src in enumerate(sources, 1):
                    st.markdown(f"**{i}.** `{src}`")
            else:
                st.write("No source metadata available.")

        except Exception as e:
            st.error(f"Something went wrong: {e}")