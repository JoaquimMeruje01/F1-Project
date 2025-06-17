import streamlit as st
import pandas as pd
import data
import plotly.express as px


def app():

    st.title("ML Predictions")

    st.write("In Machine Learning Predictions... - Under Construction")

    prediction_winner_races()
    give_spacing(2)
    prediction_dnf()
    give_spacing(2)
    prediction_change_team()



def prediction_winner_races():
     
     st.markdown("### Race Winners")



def prediction_dnf():
     
     st.markdown("### Race DNFs")



def prediction_change_team():
     
     st.markdown("### Team Changes next Season")



def give_spacing(number_lines):
     
     for i in range(0, number_lines):
          st.write(" ")    

