# ---------------------------------------- RACE STATUS ----------------------------------------

# This file allows the user to log in to the application. It checks all the information entered 
# by the user and encrypts the password

import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import data

def app():

    st.title("Race Status")

    st.write("In the Races Status page, you can discover some statistics about the number of races finished by each driver or technical problems")

    drivers_problems()
    give_spacing(2)
    teams_problems()
    give_spacing(2)
    years_problems()


def drivers_problems():

    st.markdown("### Drivers Status Races")
    
    col1_1, col1_2, col1_3  = st.columns([0.25, 0.25, 0.5])
    with col1_1:
            min_total_races = st.number_input('Minimum of Total Races', min_value=30, max_value=200, value=50)
    with col1_2:
            max_total_races = st.number_input('Maximum of Total Races', min_value=200, max_value=350, value=250) 
    with col1_3:
            pass             
        
    col1, col2 = st.columns([0.5, 0.5])

    with col1:

        st.markdown("##### Top 10 Drivers with more DNFs")

        df_moreDNFs = pd.read_csv("dataframes/race_counts.csv")
        df_moreDNFs = df_moreDNFs[(df_moreDNFs['Total Races'] > min_total_races) & (df_moreDNFs['Total Races'] < max_total_races)]
        df_moreDNFs = df_moreDNFs.drop(columns=['Finished Races (%)','Total Health', 'Total + Laps'])
        df_moreDNFs = df_moreDNFs.sort_values(by=['Total DNFs','Total Races'], ascending=False).head(10)
        df_moreDNFs.reset_index(drop=True)
        df_moreDNFs.index = range(1, len(df_moreDNFs) + 1)
        st.dataframe(df_moreDNFs)    

        st.markdown("##### Top 10 Drivers with more + Laps")

        df_moreLaps = pd.read_csv("dataframes/race_counts.csv")
        df_moreLaps = df_moreLaps[(df_moreLaps['Total Races'] > min_total_races) & (df_moreLaps['Total Races'] < max_total_races)]
        df_moreLaps = df_moreLaps.drop(columns=['Finished Races (%)','Total Health', 'Total DNFs'])
        df_moreLaps = df_moreLaps.sort_values(by=['Total + Laps','Total Races'], ascending=False).head(10)
        df_moreLaps.reset_index(drop=True)
        df_moreLaps.index = range(1, len(df_moreLaps) + 1)
        st.dataframe(df_moreLaps)
        
    with col2:

        st.markdown("##### Top 10 Drivers with more Finished Races")

        df_moreDNFs = pd.read_csv("dataframes/race_counts.csv")
        df_moreDNFs = df_moreDNFs[(df_moreDNFs['Total Races'] > min_total_races) & (df_moreDNFs['Total Races'] < max_total_races)]
        df_moreDNFs = df_moreDNFs.drop(columns=['Total Health', 'Total DNFs', 'Total + Laps'])
        df_moreDNFs = df_moreDNFs.sort_values(by=['Finished Races (%)','Total Races'], ascending=False).head(10)
        df_moreDNFs.reset_index(drop=True)
        df_moreDNFs.rename(columns={'Finished Races (%)': 'Finished (%)'}, inplace=True)
        df_moreDNFs.index = range(1, len(df_moreDNFs) + 1)
        st.dataframe(df_moreDNFs)

        st.markdown("##### Top 10 Drivers with more Health Issues")

        df_health = pd.read_csv("dataframes/race_counts.csv")
        df_health = df_health[(df_health['Total Races'] > min_total_races) & (df_health['Total Races'] < max_total_races)]
        df_health = df_health.drop(columns=['Finished Races (%)', 'Total DNFs', 'Total + Laps'])
        df_health = df_health.sort_values(by=['Total Health','Total Races'], ascending=False).head(10)
        df_health.reset_index(drop=True)
        df_health.rename(columns={'Total Health': 'Problems'}, inplace=True)
        df_health.index = range(1, len(df_health) + 1)
        st.dataframe(df_health)


def years_problems():

        df_problems_years = pd.read_csv("dataframes/race_problems_years.csv")

        st.markdown("### Problems Evolution over the years")

        columns_all = df_problems_years.columns
        columns_to_remove = ['year', 'raceId']
        columns_all = [item for item in columns_all if item not in columns_to_remove]

        columns_to_plot = st.multiselect('Parameters', columns_all, default='Total Problems')

        start, end = st.slider("Years Interval", min_value=1950, max_value=2024, value=(1950, 2024))
        df_problems_years = df_problems_years[(df_problems_years["year"] >= start) & (df_problems_years["year"] <= end)]

        fig = px.line(df_problems_years,
                      x="year",
                      y=columns_to_plot,
                      labels={"value": "Incidents", "variable": "Parameters"})

        st.plotly_chart(fig)
        

def teams_problems():
      
      st.markdown("### Teams Status Races")

      df_team_status = pd.read_csv("dataframes/teams_status.csv")

      col1, col2 = st.columns([0.5, 0.5])

      with col1:

        team_selected = st.selectbox("Team", data.teams_names, index=1)

      with col2:

        df_team_status = create_team_dataframe(team_selected, df_team_status)
        min_value_team = int(df_team_status['year'].min())
        max_value_team = int(df_team_status['year'].max())

        start, end = st.slider("Year Interval", min_value=min_value_team, max_value=max_value_team, value=(min_value_team, max_value_team))

      df_team_status = df_team_status[(df_team_status['year'] >= start) & (df_team_status['year'] <= end)]  

      st.markdown("##### Top 10 Drivers with more Total Races by Team")

      drivers_races = df_team_status.groupby("Name").size()
      finished_races = df_team_status[(df_team_status["status"] == "Finished") | (df_team_status["status"].str.contains("Lap"))].groupby("Name").size()
      engine_races = df_team_status[df_team_status["status"].isin(data.engine_columns)].groupby("Name").size()
      fuel_races = df_team_status[df_team_status["status"].isin(data.fuel_columns)].groupby("Name").size()
      transmission_races = df_team_status[df_team_status["status"].isin(data.transmission_columns)].groupby("Name").size()
      wheel_races = df_team_status[df_team_status["status"].isin(data.wheel_columns)].groupby("Name").size()
      water_oil_races = df_team_status[df_team_status["status"].isin(data.water_columns + data.oil_columns)].groupby("Name").size()

      drivers_races  = pd.DataFrame({"Total Races": drivers_races, 
                                     "Finished Races": finished_races,
                                     "Engine": engine_races,
                                     "Fuel": fuel_races,
                                     "Wheels": wheel_races,
                                     "Water/Oil": water_oil_races,
                                     "Transmission": transmission_races}).reset_index()
      drivers_races.rename(columns={'Finished Races': 'Finished (%)'}, inplace=True)

      drivers_races['Finished (%)'] = ((drivers_races ['Finished (%)'] / drivers_races ['Total Races'])*100).round(2)
      drivers_races['Engine'] = drivers_races['Engine'].fillna(0)
      drivers_races['Fuel'] = drivers_races['Fuel'].fillna(0)
      drivers_races['Wheels'] = drivers_races['Wheels'].fillna(0)
      drivers_races['Water/Oil'] = drivers_races['Water/Oil'].fillna(0)
      drivers_races['Transmission'] = drivers_races['Transmission'].fillna(0)
      
      drivers_races = drivers_races.sort_values(by=['Total Races', 'Finished (%)'], ascending=False).head(10)
      drivers_races.index = range(1, len(drivers_races) + 1)
      st.dataframe(drivers_races) 

      col3, col4 = st.columns([0.72, 0.28])

      with col3:

        st.markdown("##### Points lost from the starting grid with a DNF")

        df_points_lost = pd.read_csv("dataframes/teams_points_lost.csv")
        df_points_lost = create_team_dataframe(team_selected, df_points_lost)
        df_points_lost = df_points_lost[(df_points_lost['year'] >= start) & (df_points_lost['year'] <= end)]  
        drivers_races = df_points_lost.groupby("Name").size()
        points_lost = df_points_lost.groupby("Name")["Points Lost"].sum()
        points_lost = points_lost.sort_values(ascending=False).head(8)

        chart_data = pd.DataFrame({
          'Drivers': points_lost.index,
          'Lost Points': points_lost.values
        })


        bar_chart = alt.Chart(chart_data).mark_bar(size=20).encode(
               x=alt.X('Lost Points:Q', axis=alt.Axis(title='Lost Points', titleFontSize=14, labelFontSize=12)),
               y=alt.Y('Drivers:O', sort='-x', axis=alt.Axis(title='Drivers', titleFontSize=14, labelFontSize=12)),
               color=alt.value('#CE2D1E')).properties(height=300,width=500).configure(background='#15151D')
        st.altair_chart(bar_chart)

      with col4:

        st.markdown("##### Teams Evolution")

        write_table_evolution_names(team_selected)


def create_team_dataframe(team_name, dataframe):

      team_record_names = data.team_mapping.get(team_name)  

      if team_name == 'Mercedes':
           dataframe = dataframe[dataframe['year'] >= 1970]
      elif team_name == 'Aston Martin':
           dataframe = dataframe[dataframe['year'] >= 1991]   
      elif team_name == 'Sauber':
           dataframe = dataframe[dataframe['year'] >= 1993]       
      elif team_name == 'Alpine':
           dataframe = dataframe[dataframe['year'] >= 1981]          
           
      dataframe = dataframe[dataframe['Team Name'].isin(team_record_names)]        

      return(dataframe)


def write_table_evolution_names(team_selected):

     team_record_names = data.team_mapping.get(team_selected)
     years_list = data.teams_years_list[data.teams_names.index(team_selected)]

     if len(team_record_names) == 1:
          st.write(f"""
               | Start Year | Team Name          |
               |------------|--------------------|
               |   {years_list[0]}   | {team_record_names[0]} | 
          """)
     elif len(team_record_names) == 2:
          st.write(f"""
               | Start Year | Team Name          |
               |------------|--------------------|
               |   {years_list[0]}   | {team_record_names[0]} | 
               |   {years_list[1]}   | {team_record_names[1]} |     
          """)
     elif len(team_record_names) == 3:
          st.write(f"""
               | Start Year | Team Name          |
               |------------|--------------------|
               |   {years_list[0]}   | {team_record_names[0]} | 
               |   {years_list[1]}   | {team_record_names[1]} |     
               |   {years_list[2]}   | {team_record_names[2]} |     
          """)
     elif len(team_record_names) == 4:
          st.write(f"""
               | Start Year | Team Name          |
               |------------|--------------------|
               |   {years_list[0]}   | {team_record_names[0]} | 
               |   {years_list[1]}   | {team_record_names[1]} |     
               |   {years_list[2]}   | {team_record_names[2]} |     
               |   {years_list[3]}   | {team_record_names[3]} |     
          """)
     elif len(team_record_names) == 5:
          st.write(f"""
               | Start Year | Team Name          |
               |------------|--------------------|
               |   {years_list[0]}   | {team_record_names[0]} | 
               |   {years_list[1]}   | {team_record_names[1]} |     
               |   {years_list[2]}   | {team_record_names[2]} |     
               |   {years_list[3]}   | {team_record_names[3]} |     
               |   {years_list[4]}   | {team_record_names[4]} |     
          """)
     elif len(team_record_names) == 6:
          st.write(f"""
               | Start Year | Team Name          |
               |------------|--------------------|
               |   {years_list[0]}   | {team_record_names[0]} | 
               |   {years_list[1]}   | {team_record_names[1]} |     
               |   {years_list[2]}   | {team_record_names[2]} |     
               |   {years_list[3]}   | {team_record_names[3]} |     
               |   {years_list[4]}   | {team_record_names[4]} |     
               |   {years_list[5]}   | {team_record_names[5]} |     
          """)
     else:
          st.write("Too many teams to display!")
    


def give_spacing(number_lines):
     
     for i in range(0, number_lines):
          st.write(" ")

