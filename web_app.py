# ------------------------------------------ WEB-APP ------------------------------------------

# This file is responsible for connecting all the project modules and starting the system. If you 
# want to open the application, you will need to run this file, according to the following command:
# -> streamlit run web_app.py

import streamlit as st
from streamlit_option_menu import option_menu
import drivers_teams, race_status, homepage, circuits, ML_predictions

st.set_page_config(page_title="F1 Analysis and Prediction Project")

class Multiapp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function   
        })

    def run():
        with st.sidebar:
            app = option_menu(
                menu_title='F1 Project',
                menu_icon='bi bi-database-check',
                options=['Homepage', 'Drivers and Teams', 'Circuits', 'Races Status', 'ML Predictions'],
                icons=['house-fill', 'bi bi-stoplights', 'bi bi-stopwatch-fill', 'bi bi-tools', 'bi bi-cpu'],
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'#15151D'},
                    "icon": {"color": "#FFFFFF", "font-size": "20px"}, 
                    "nav-link": {"color":"#FFFFFF","font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#CE2D1E"},
                    "nav-link-selected": {"background-color": "#CE2D1E"}}
            ) 

        if app == "Homepage":
            homepage.app()
        if app == "Drivers and Teams":
            drivers_teams.app()
        if app == "Circuits":
            circuits.app()    
        if app == "Races Status":
            race_status.app()    
        if app == "ML Predictions":
            ML_predictions.app()      

    run()    