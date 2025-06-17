# ------------------------------------------ HOMEPAGE ------------------------------------------

# This file is responsible for displaying the application's home page, which provides the user 
# with a description of how the project works

import streamlit as st
from PIL import Image

def app():

    st.title("Homepage")

    st.write("Welcome to F1 Project, a Data Science and Machine Learning Project, developed to analyse and predict cool and fresh \
              information about Formula 1! Here, you'll find interactive visualisations, predictive models and fascinating statistics \
              about F1's most iconic drivers, teams, circuits and even race statuses.")
    
    image = Image.open("Images/logo.jpg")
    st.image(image, use_column_width=True, width=200)

    st.write("The main goals of this project include analyse historical data from races, classifications from different drivers and seasons;\
              analyse historical data from races and classifications from different drivers and seasons; visualise statistics intuitively and\
              interactively about drivers, teams, circuits and race statuses and build Machine Learning models to predict race winners,\
              dnfs and team changes for next seasons.")

    st.write("**The Streamlit app is split into five pages:**")
    st.write("1) Homepage: project overview, goals, and technologies used to develop the project;")
    st.write("2) Drivers and Teams: statistics, performances, and trends among drivers and constructors;")
    st.write("3) Circuits: historical data and key insights for each Grand Prix circuit;")
    st.write("4) Races Status: statistics and visualisations about dnfs and cars problems over the seasons;")
    st.write("5) ML Predictions: machine learning models to predict race outcomes, dnfs and team changes.")

    st.write("This project was developed with Python programming language and the Streamlit framework, joint with some libraries such \
             as Numpy, Pandas, Seaborn, Plotly and Scikit-learn. Data was collected from real-world datasets in Kaggle\
             and from wikipedia pages.")
    
    st.write("You can find more information about the project and respective code in the GitHub repository: ")

    st.write("Start the engine, open the charts and enjoy the science behind the speed!")
   
    st.write("Kaggle Source: https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020")

