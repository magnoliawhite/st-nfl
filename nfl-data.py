import yfinance as yf
import streamlit as st
import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(page_title='NFL Analysis', page_icon= ':bar_chart:', layout="wide")

st.write("""
# Basic National Football League Dashboard
""")

st.markdown('#')

df = pd.read_csv('Ex_Scatter.csv')
df1 = pd.read_csv('Ex_Time_Series.csv')
df2 = pd.read_csv('Ex_Bar.csv')
df3 = pd.read_csv('Ex_Pie.csv')

col1, col2 = st.columns([1.66,1])

with col1:
    fig = px.scatter(
        df,
        x = "Yards Per Game",
        y = "Touchdowns",
        hover_data=['Player'],
        color="Player",
        title = "Regression Between Y/G & TDs (2021 Season)",
        width = 1000,
        height = 600
        )
    fig.update_traces(marker_size=8)
    fig.update_layout(title_font_size=24)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig3 = px.pie(
        df3,
        values="Number_of_Quarterbacks",
        names="Group",
        title="2021 Season Quarterbacks by Age",
        width=1000,
        height=600
    )
    fig3.update_layout(title_font_size=24)
    st.plotly_chart(fig3, use_container_width=True)

with st.container():
    fig1 = px.line(
        df1,
        x = "Season",
        y = "Yds",
        title = "Historical Average Passing Yards Per Game by Season",
        width = 1300,
        height = 500
        )
    fig1.update_layout(title_font_size=24)
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.bar(
        df2,
        x = "Week",
        y = "Total_Yards",
        hover_name='Type',
        color="Type",
        barmode='group',
        title = "Detroit Lions 2021 Total Yards Through Week 15",
        width = 1400,
        height = 500
        )
    fig2.update_layout(title_font_size=24)
    st.plotly_chart(fig2, use_container_width=True)

