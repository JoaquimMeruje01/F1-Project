import streamlit as st
import pandas as pd
import data
import plotly.express as px


def app():

    st.title("ML Predictions")

    st.write("In ML Predictions, you can explore race outcomes forecasted by machine learning models. Some of teh interesing results" \
    "include podium finishes, championship rankings and DNF probabilities.")

    prediction_winner_races()
    give_spacing(3)
    prediction_championship_rankings()
    give_spacing(2)
    prediction_dnf() 


def prediction_winner_races():
     
     st.markdown("### Race Podium Predictions")

     podiums = pd.read_csv(r"C:\Users\Joaquim Meruje\OneDrive\Documentos\F1-Project-Original\dataframes\predictions_podiums.csv")

     col1, col2 = st.columns([0.5, 0.5])

     with col1:
          race_year = podiums[podiums["year"] >= 1980]["year"].unique().tolist()
          race_year.sort(reverse=True)
          year_selected = st.selectbox("Year", race_year) 
          podiums = podiums[podiums['year'] == year_selected] 

     with col2:
          circuits_name = podiums["Circuit Name"].unique().tolist()
          circuits_name.sort()
          circuit_selected = st.selectbox("Circuit Name", circuits_name)
          podiums = podiums[podiums['Circuit Name'] == circuit_selected]        

     pred_podium = (podiums.sort_values('pred_position').head(3)
               .apply(lambda row: f"{row['Driver Name']} ({row['Team Name']})", axis=1).tolist())

     real_podium = (podiums.sort_values('positionOrder').head(3)
               .apply(lambda row: f"{row['Driver Name']} ({row['Team Name']})", axis=1).tolist())

     colA, colB = st.columns(2)

     with colA:
          st.markdown("#### 🏆 Predicted Podium")
          for i, driver in enumerate(pred_podium, start=1):
               st.markdown(f"**{i}.** {driver}")

     with colB:
          st.markdown("#### 🎯 Real Podium")
          for i, driver in enumerate(real_podium, start=1):
               st.markdown(f"**{i}.** {driver}")


def prediction_championship_rankings():
     
     st.markdown("### Championship Rankings Predictions")

     rankings_drivers = pd.read_csv(r"C:\Users\Joaquim Meruje\OneDrive\Documentos\F1-Project-Original\dataframes\drivers_championships_prediction.csv")

     col1, col2 = st.columns([0.5, 0.5])
     
     with col1:
          race_year = rankings_drivers[rankings_drivers["year"] >= 1980]["year"].unique().tolist()
          race_year.sort(reverse=True)
          year_selected = st.selectbox("Year Classification", race_year, index=0) 
          rankings_drivers = rankings_drivers[rankings_drivers['year'] == year_selected] 
     with col2:
          drivers_or_teams = st.selectbox("Championship", ["Drivers", "Teams"], index=0) 

     if drivers_or_teams == "Drivers":  

          colA, colB = st.columns([0.5, 0.5])
          with colA:
               st.markdown("#### 🏆 Predicted Championship")

               rankings_drivers_v2 = rankings_drivers.drop(columns=['year'])
               rankings_drivers_v2.rename(columns={'Predicted Points': 'Points'}, inplace=True)
               rankings_drivers_v2.index = range(1, len(rankings_drivers_v2) + 1)
               st.dataframe(rankings_drivers_v2) 
          with colB:
               st.markdown("#### 🎯 Real Championship")   

               drivers_champ =pd.read_csv(r"C:\Users\Joaquim Meruje\OneDrive\Documentos\F1-Project-Original\dataframes\drivers_championships.csv") 
               drivers_champ = drivers_champ[drivers_champ['year'] == year_selected]      
               drivers_champ = drivers_champ.drop(columns=['driverId', 'race_entries', 'fastestLapSpeed', 'pole_position', 'podium', 'victory', 'final_position'])
               drivers_champ.rename(columns={'points': 'Points'}, inplace=True)
               drivers_champ.index = range(1, len(drivers_champ) + 1)
               drivers_champ = drivers_champ[['driverName', 'Team Name', 'Points']]
               st.dataframe(drivers_champ)
     else:  

          colA, colB = st.columns([0.5, 0.5])
          with colA:
               st.markdown("#### 🏆 Predicted Championship")

               rankings_teams = (rankings_drivers.groupby(['year', 'Team Name'], as_index=False)['Predicted Points'].sum()) 
               rankings_teams = rankings_teams.sort_values(by='Predicted Points', ascending=False)
               rankings_teams = rankings_teams.drop(columns=['year'])
               rankings_teams.rename(columns={'Predicted Points': 'Points'}, inplace=True)
               rankings_teams.index = range(1, len(rankings_teams) + 1)
               st.dataframe(rankings_teams) 
          with colB:
               st.markdown("#### 🎯 Real Championship")    

               teams_champ = pd.read_csv(r"C:\Users\Joaquim Meruje\OneDrive\Documentos\F1-Project-Original\dataframes\constructors_championships.csv")         
               teams_champ = teams_champ[teams_champ['year'] == year_selected] 
               teams_champ = teams_champ.drop(columns=['wins', 'constructorId', 'date', 'positionText', 'position', 'year'])
               teams_champ.rename(columns={'points': 'Points'}, inplace=True)
               teams_champ.index = range(1, len(teams_champ) + 1)
               teams_champ = teams_champ[['Team Name', 'Points']]
               st.dataframe(teams_champ) 

     
def prediction_dnf():
     
     st.markdown("### Race DNFs Predictions")

     st.write("Under Construction...")


def give_spacing(number_lines):
     
     for i in range(0, number_lines):
          st.write(" ")    

