import streamlit as st
import polars as pl
import polars.selectors as cs
import plotly.express as px
import duckdb

df = pl.read_csv("global_inflation_data.csv", try_parse_dates=True)

st.title("Global inflation since 1980")
st.write("### This project was made for my personal studies and to practice my skills in data analysis and visualization.")


df_melted = df.melt(id_vars=["country_name"], variable_name="year", value_name="inflation")

country_list = df_melted["country_name"]
selected_country = st.selectbox("Select a country", country_list)


result = duckdb.sql(f"SELECT country_name, year, inflation FROM df_melted WHERE country_name = '{selected_country}' AND inflation IS NOT NULL ").to_df()


fig = px.line(result, x="year", y="inflation", title=f"Inflation in {selected_country}")

st.plotly_chart(fig)

