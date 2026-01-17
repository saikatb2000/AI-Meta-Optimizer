import streamlit as st
from fetch_meta import fetch_meta
from gemini_ai import optimize_meta

st.set_page_config(page_title="SEO Meta Optimizer AI", layout="centered")

st.title("AI Meta Optimizer")
st.markdown("*by Saikat Bhattacharjee*")
st.write("Fetch and optimize meta title & description using AI")

url = st.text_input("Enter Website URL")

if st.button("Analyze & Optimize"):

    if url.strip() == "":
        st.warning("Please enter a valid URL")
    else:
        with st.spinner("Fetching meta data..."):
            title, description = fetch_meta(url)

        st.subheader("Current Meta Data")
        st.write("**Title:**", title)
        st.write("**Description:**", description)

        with st.spinner("Generating AI optimized meta..."):
            optimized = optimize_meta(title, description, url)

        st.subheader("AI Optimized SEO Meta")
        st.code(optimized)
