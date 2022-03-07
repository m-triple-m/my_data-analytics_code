import streamlit as st
from analyseData import AnalyseData
from visualizeData import *

mydata = AnalyseData('Pokemon.csv')

st.dataframe(mydata.df)

fig = scatter3D(mydata.df, 'HP', 'Attack',
                'Defense', 'Type 1', 'Generation')

st.plotly_chart(fig, use_container_width=True)


fig1 = scatter3D(mydata.df, 'HP', 'Attack',
                 'Defense', 'Type 1', 'Generation')

st.plotly_chart(fig1, use_container_width=True)
