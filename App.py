import streamlit as st
import polars as pl
import matplotlib.pyplot as plt

df = pl.read_csv("global_inflation_data.csv")

st.write("""# Global inflation since 1980""")
st.write("""### Made by [me](https://www.linkedin.com/in/lucasehara/)""")

st.write(df) 