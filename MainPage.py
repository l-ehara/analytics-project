import streamlit as st
import polars as pl
import plotly.express as px

df = pl.read_csv("global_inflation_data.csv", try_parse_dates=True)

st.write("# Global inflation since 1980")
st.write("### This project was made for my personal studies and to practice my skills in data analysis and visualization.")

country = st.selectbox("Select a country", df['country_name'])

st.write(df)
