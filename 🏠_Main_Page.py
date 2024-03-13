import streamlit as st
import polars as pl
import polars.selectors as cs
import plotly.express as px
import duckdb 
from jinja2 import Template


st.set_page_config(
    page_title="Global Infaltion Analytics Project",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="auto",
)

df = pl.read_csv("global_inflation_data.csv", try_parse_dates=True)

st.title("Global inflation since 1980")
st.write("##### This project was made for my personal studies and to practice my skills in data analysis and visualization.")

df_melted = df.melt(id_vars=["country_name"], variable_name="year", value_name="inflation")

country_list = df_melted["country_name"]
selected_country = st.selectbox("Select a country", country_list.unique().sort(), index = 24)

query_file_path = 'sql/inflation_by_country_by_period.sql'  
with open(query_file_path, 'r') as file:
    template = Template(file.read())
    sql_query = template.render(selected_country=selected_country)

result = duckdb.execute(sql_query).fetchdf()

fig = px.line(result, x="year", y="inflation", title=f"Inflation in {selected_country}")
fig.update_layout(
    dragmode='pan'
)
left_col, center_col, right_col = st.columns([0.01 , 6, 0.01])
with center_col: 
    st.plotly_chart(fig, use_container_width=True)
    st.table(result)