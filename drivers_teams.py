import streamlit as st
import pandas as pd
import data
import plotly.express as px
import ast


def app():

    st.title("Drivers and Teams")

    st.write("In Drivers and Teams you can discover more about your favourite drivers and teams. Since simple stats about championships, number of points or wins, until more complex statistics over the years.")

    drivers_info()
    give_spacing(2)
    team_info()


def drivers_info():
     
     st.markdown("### Drivers Results")

     df_drivers = pd.read_csv("dataframes/drivers.csv")
     start_year = int(df_drivers['dob'].str[:4].min())
     end_year = max_year = int(df_drivers['dob'].str[:4].max()) 

     drivers_names= df_drivers.copy()
     nacionality_selected = 'British'
     start_year = df_drivers['dob'].str[:4].min()
     end_year = df_drivers['dob'].str[:4].max()

     col1, col2, col3 = st.columns([0.35, 0.35, 0.3])

     with col1:
          drivers_country = df_drivers["nationality"].unique().tolist()
          drivers_country.sort()
          nacionality_selected = st.selectbox("Nationality", drivers_country, index=9)

     with col2:
          min_year = int(df_drivers['dob'].str[:4].min())
          max_year = int(df_drivers['dob'].str[:4].max())
          start_year, end_year = st.slider("Birth Year", min_value=min_year, max_value=max_year, value=(min_year, max_year))

     with col3:
          drivers_names = drivers_names[drivers_names['nationality'] == nacionality_selected]
          drivers_names = drivers_names[
               (drivers_names['dob'].str[:4].astype(int) >= start_year) & 
               (drivers_names['dob'].str[:4].astype(int) <= end_year)]
          drivers_names = drivers_names["name"].unique().tolist()
          drivers_names.sort()
          if nacionality_selected == 'British':
               name_selected = st.selectbox("Driver Name", drivers_names, index=110)
          else:  
               name_selected = st.selectbox("Driver Name", drivers_names)   

     colA, colB, colC = st.columns([0.33, 0.33, 0.33])

     df_drivers_championships = pd.read_csv("dataframes/drivers_championships.csv")
     df_drivers_championships = df_drivers_championships[df_drivers_championships['driverName'] == name_selected]

     df_drivers_v2 = pd.read_csv("dataframes/drivers_data.csv")
     df_drivers_v2 = df_drivers_v2[df_drivers_v2['driverName'] == name_selected]

     df_drivers_teams_by_season = pd.read_csv("dataframes/drivers_teams_by_season.csv")
     df_drivers_teams_by_season['drivers'] = df_drivers_teams_by_season['drivers'].apply(ast.literal_eval)
     driver_rows = df_drivers_teams_by_season[df_drivers_teams_by_season['drivers'].apply(lambda x: name_selected in x)]
     teammates = driver_rows['drivers'].apply(lambda x: [driver for driver in x if driver != name_selected]).explode().dropna().unique().tolist()

     with colA:     

          if 'code' in df_drivers_v2.columns and 'number' in df_drivers_v2.columns:
               if pd.isna(df_drivers_v2['code'].iloc[0]) and pd.isna(df_drivers_v2['number'].iloc[0]):
                    code_number = "-----"
               elif pd.isna(df_drivers_v2['number'].iloc[0]):
                    code_number = str(df_drivers_v2['code'].iloc[0])    
               else:
                    code_number = str(df_drivers_v2['code'].iloc[0]) + ' - ' + str(int(df_drivers_v2['number'].iloc[0]))
          else:
               code_number = "-----"


          container = f"""
                    <div style='padding: 3.5px; background-color: #CE2D1E; border-radius: 6px; width: 220px; height: 210px; display: flex; flex-direction: column;'>
                        <div style='display: flex; align-items: center; justify-content: space-between;'>
                            <h3 style='margin-top: 0.01px; font-size: 19px; line-height: 1.4;'><strong>Personal Statistics</strong></h3>
                        </div>
                        <div style='font-size: 13px;'>
                            <p style='line-height: 0.9;'>• Name: {name_selected}</p>  
                            <p style='line-height: 0.9;'>• Birthday: {df_drivers_v2['dob'].iloc[0]}</p> 
                            <p style='line-height: 0.9;'>• Code and Number : {code_number}</p>  
                            <p style='line-height: 0.9;'>• Number of Teams: {len(df_drivers_championships['Team Name'].value_counts())}</p>
                            <p style='line-height: 0.9;'>• Number of Team-mates: {len(teammates)}</p>
                        </div>
                    </div>
                    """
            
          st.markdown(container, unsafe_allow_html=True)

     with colB:

          container = f"""
                    <div style='padding: 3.5px; background-color: #CE2D1E; border-radius: 6px; width: 220px; height: 210px; display: flex; flex-direction: column;'>
                        <div style='display: flex; align-items: center; justify-content: space-between;'>
                            <h3 style='margin-top: 0.01px; font-size: 19px; line-height: 1.4;'><strong>Race Statistics</strong></h3>
                        </div>
                        <div style='font-size: 13px;'>
                            <p style='line-height: 0.9;'>• Number of Seasons: {len(df_drivers_championships)}</p>
                            <p style='line-height: 0.9;'>• Number of Entries: {df_drivers_championships['race_entries'].sum()}</p>
                            <p style='line-height: 0.9;'>• Number of Wins: {df_drivers_championships['victory'].sum()}</p>
                            <p style='line-height: 0.9;'>• Number of Podiums: {df_drivers_championships['podium'].sum()}</p>
                            <p style='line-height: 0.9;'>• Number of Poles: {df_drivers_championships['pole_position'].sum()}</p>
                        </div>
                    </div>
                    """
            
          st.markdown(container, unsafe_allow_html=True)

     with colC:

          container = f"""
                         <div style='padding: 4.5px; background-color: #CE2D1E; border-radius: 6px; width: 220px; height: 210px; display: flex; flex-direction: column;'>
                         <div style='display: flex; align-items: center; justify-content: space-between;'>
                              <h3 style='margin-top: 0.01px; font-size: 19px; line-height: 1.4;'><strong>Championships Statistics</strong></h3>
                         </div>
                         <div style='font-size: 13px;'>
                              <p style='line-height: 0.9;'>• Drivers 1º Championships: {(df_drivers_championships['final_position'] == 1.0).sum()}</p>
                              <p style='line-height: 0.9;'>• Drivers 2º Championships: {(df_drivers_championships['final_position'] == 2.0).sum()}</p>
                              <p style='line-height: 0.9;'>• Drivers 3º Championships: {(df_drivers_championships['final_position'] == 3.0).sum()}</p>
                              <p style='line-height: 0.9;'>• Drivers 4º Championships: {(df_drivers_championships['final_position'] == 4.0).sum()}</p>
                              <p style='line-height: 0.9;'>• Drivers 5º Championships: {(df_drivers_championships['final_position'] == 5.0).sum()}</p>
                         </div>
                         </div>
                         """
               
          st.markdown(container, unsafe_allow_html=True) 

     give_spacing(1)

     st.markdown("##### Teams Evolution")
     write_table_evolution_names_for_drivers(df_drivers_championships, name_selected) 
     
     give_spacing(2)

     df_drivers_championships_copy = df_drivers_championships
     df_drivers_championships_copy = df_drivers_championships_copy.drop(columns=['driverId', 'driverName', 'Team Name'])
     df_drivers_championships_copy['year'] = df_drivers_championships_copy['year'].astype(str)
     df_drivers_championships_copy = df_drivers_championships_copy.rename(columns={
                                                                      'fastestLapSpeed': 'Fastest Speed',
                                                                      'final_position': 'Championship Positions',
                                                                      'pole_position': 'Poles',
                                                                      'podium': 'Podiums',
                                                                      'victory': 'Wins',
                                                                      'points': 'Points',
                                                                      'race_entries': 'Entries',
                                                                      'year': 'Years'})

     df_drivers_championships_copy.reset_index(drop=True)
     df_drivers_championships_copy.index = range(1, len(df_drivers_championships_copy) + 1)   

     st.markdown("##### Results Over the Years") 
     
     columns_all = ['Points', 'Wins', 'Podiums', 'Poles', 'Championship Positions', 'Fastest Speed', 'Entries']
     columns_to_plot = st.selectbox('Statistics', columns_all, index=0)

     if columns_to_plot == 'Fastest Speed' and df_drivers_championships_copy['Fastest Speed'].isnull().all():
          st.warning("At this time, there was not any register about fastest speed")
     else:     
          fig = px.line(df_drivers_championships_copy,
                    x="Years",
                    y=columns_to_plot)

          st.plotly_chart(fig)


def team_info():

    st.markdown("### Teams Results")

    df_teams = pd.read_csv(r"dataframes/teams.csv")

    col1, col2 = st.columns([0.5, 0.5])

    with col1:

        team_selected = st.selectbox("Team", data.teams_names, index=1)

    with col2:

        df_teams = create_team_dataframe(team_selected, df_teams)
        min_value_team = int(df_teams['year'].min())
        max_value_team = int(df_teams['year'].max())

        start, end = st.slider("Year Interval", min_value=min_value_team, max_value=max_value_team, value=(min_value_team, max_value_team))

    df_teams = df_teams[(df_teams['year'] >= start) & (df_teams['year'] <= end)]      

    colA, colB, colC = st.columns([0.32, 0.35, 0.33])

    with colA:        

        container = f"""
                    <div style='padding: 3.5px; background-color: #CE2D1E; border-radius: 6px; width: 200px; height: 239px; display: flex; flex-direction: column;'>
                        <div style='display: flex; align-items: center; justify-content: space-between;'>
                            <h3 style='margin-top: 0.01px; font-size: 19px; line-height: 1.4;'><strong>Race Statistics</strong></h3>
                        </div>
                        <div style='font-size: 13px;'>
                            <p style='line-height: 0.9;'>• Number of Entries: {len(df_teams)/2}</p>
                            <p style='line-height: 0.9;'>• Number of Wins: {(df_teams['position'] == 1).sum()}</p>
                            <p style='line-height: 0.9;'>• Number of Podiums: {(df_teams['position'] < 4).sum()}</p>
                            <p style='line-height: 0.9;'>• Number of Points: {df_teams['points'].sum()}</p>
                            <p style='line-height: 0.9;'>• Number of Poles: {(df_teams['grid'] == 1).sum()}</p>
                            <p style='line-height: 0.9;'>• Number of Front Starts: {(df_teams['grid'] < 3).sum()}</p>
                        </div>
                    </div>
                    """
            
        st.markdown(container, unsafe_allow_html=True)

    with colB:

        st.markdown("##### Teams Evolution")
        write_table_evolution_names(team_selected)

    with colC:

        df_drivers_championships = pd.read_csv("dataframes/drivers_championships.csv")
        df_constructors_championships = pd.read_csv("dataframes/constructors_championships.csv")

        df_drivers_championships = create_team_dataframe(team_selected, df_drivers_championships) 
        df_constructors_championships = create_team_dataframe(team_selected, df_constructors_championships) 

        df_drivers_championships = df_drivers_championships[(df_drivers_championships['year'] >= start) & (df_drivers_championships['year'] <= end)] 
        df_constructors_championships = df_constructors_championships[(df_constructors_championships['year'] >= start) & (df_constructors_championships['year'] <= end)] 

        container = f"""
                    <div style='padding: 4.5px; background-color: #CE2D1E; border-radius: 6px; width: 255px; height: 239px; display: flex; flex-direction: column;'>
                        <div style='display: flex; align-items: center; justify-content: space-between;'>
                            <h3 style='margin-top: 0.01px; font-size: 19px; line-height: 1.4;'><strong>Titles Statistics</strong></h3>
                        </div>
                        <div style='font-size: 13px;'>
                            <p style='line-height: 0.9;'>• Drivers 1º Championships: {(df_drivers_championships['final_position'] == 1.0).sum()}</p>
                            <p style='line-height: 0.9;'>• Drivers 2º Championships: {(df_drivers_championships['final_position'] == 2.0).sum()}</p>
                            <p style='line-height: 0.9;'>• Drivers 3º Championships: {(df_drivers_championships['final_position'] == 3.0).sum()}</p>
                            <p style='line-height: 0.9;'>• Constructors 1º Championships: {(df_constructors_championships['position'] == 1.0).sum()}</p>
                            <p style='line-height: 0.9;'>• Constructors 2º Championships: {(df_constructors_championships['position'] == 2.0).sum()}</p>
                            <p style='line-height: 0.9;'>• Constructors 3º Championships: {(df_constructors_championships['position'] == 3.0).sum()}</p>
                        </div>
                    </div>
                    """
            
        st.markdown(container, unsafe_allow_html=True) 

    give_spacing(1)

    st.markdown("##### Statistics for every driver")  

    df_drivers_championships = df_drivers_championships.groupby('driverName', as_index=False).agg({
                                                                    'race_entries': 'sum', 
                                                                    'points': 'sum',
                                                                    'victory': 'sum',
                                                                    'podium': 'sum',
                                                                    'pole_position': 'sum',
                                                                    'fastestLapSpeed': 'max',
                                                                    'year': ['min', 'max']})
        
    df_drivers_championships.columns = ['Driver Name', 'Entries','Points', 'Wins', 'Podiums', 'Poles', 'Max Speed', 'year_start', 'year_end']
    df_drivers_championships = df_drivers_championships.sort_values(by=['year_start', 'year_end'], ascending=[True, False])
    df_drivers_championships['Duration'] = df_drivers_championships['year_start'].astype(str) + ' - ' + df_drivers_championships['year_end'].astype(str) 
    df_drivers_championships = df_drivers_championships.drop(columns=['year_start', 'year_end'])  
    df_drivers_championships.columns = [col.capitalize() for col in df_drivers_championships.columns]  
    df_drivers_championships.reset_index(drop=True)
    df_drivers_championships.index = range(1, len(df_drivers_championships) + 1)  
    st.dataframe(df_drivers_championships)


    df_graph = pd.read_csv("dataframes/constructors_championships.csv")
    df_graph = create_team_dataframe(team_selected, df_graph) 
    df_graph = df_graph[(df_graph['year'] >= start) & (df_graph['year'] <= end)] 
    df_graph = df_graph.drop(columns=['constructorId', 'positionText', 'date', 'Team Name'])  
    df_graph['year'] = df_graph['year'].astype(str)
    df_graph = df_graph[['year', 'points', 'wins', 'position']]
    df_graph.columns = [col.capitalize() for col in df_graph.columns]
    df_graph.reset_index(drop=True)
    df_graph.index = range(1, len(df_graph) + 1)      

    st.markdown("##### Champioship Statistics Evolution over the Seasons") 
     
    columns_all = ['Points', 'Wins', 'Position']
    columns_to_plot = st.selectbox('Statistics', columns_all, index=0)

    fig = px.line(df_graph,
                  x="Year",
                  y=columns_to_plot)

    st.plotly_chart(fig)


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


def write_table_evolution_names_for_drivers(df, name_selected):

     df = df.sort_values(by=['driverId', 'year'])
     df['team_transition'] = (df['Team Name'] != df['Team Name'].shift()).cumsum()
     df = df.groupby(['team_transition', 'Team Name'])['year'].agg(['min', 'max']).reset_index()
     df.columns = ['team_transition', 'Team Name', 'first_year', 'last_year']

     team_names_list = df['Team Name'].tolist()
     first_years_list = df['first_year'].tolist()
     last_years_list = df['last_year'].tolist()

     team_mates_list = []
     drivers_teams_by_season = pd.read_csv("dataframes/drivers_teams_by_season.csv")

     for i, (first_year, last_year, team_name) in enumerate(zip(first_years_list, last_years_list, team_names_list)):
          df_aux = drivers_teams_by_season[
               (drivers_teams_by_season['year'] >= first_year) &
               (drivers_teams_by_season['year'] <= last_year) &
               (drivers_teams_by_season['Team Name'] == team_name)
          ]
          df_aux['drivers'] = df_aux['drivers'].apply(lambda x: eval(x) if isinstance(x, str) else x)
          driver_rows = df_aux[df_aux['drivers'].apply(lambda x: name_selected in x)]
          team_mates = driver_rows['drivers'].apply(lambda x: [driver for driver in x if driver != name_selected and driver != 'Oliver Bearman']).explode().dropna().unique().tolist()
          team_mates_list.append(', '.join(team_mates) if team_mates else 'N/A')
          

     if len(df) == 1:
          st.write(f"""
               | Start Year    | End Year    | Team Name | Drivers in the same Team |
               |---------------|-------------|-----------|--------------------------|  
               |   {first_years_list[0]}   | {last_years_list[0]} | {team_names_list[0]} | {team_mates_list[0]} |
          """)
     elif len(df) == 2:
          st.write(f"""
               | Start Year    | End Year    | Team Name | Drivers in the same Team |
               |---------------|-------------|-----------|--------------------------|  
               |   {first_years_list[0]}   | {last_years_list[0]} | {team_names_list[0]} | {team_mates_list[0]} |  
               |   {first_years_list[1]}   | {last_years_list[1]} | {team_names_list[1]} | {team_mates_list[1]} |     
          """)
     elif len(df) == 3:
          st.write(f"""
               | Start Year    | End Year    | Team Name | Drivers in the same Team |
               |---------------|-------------|-----------|--------------------------|  
               |   {first_years_list[0]}   | {last_years_list[0]} | {team_names_list[0]} | {team_mates_list[0]} |  
               |   {first_years_list[1]}   | {last_years_list[1]} | {team_names_list[1]} | {team_mates_list[1]} |     
               |   {first_years_list[2]}   | {last_years_list[2]} | {team_names_list[2]} | {team_mates_list[2]} |    
          """)
     elif len(df) == 4:
          st.write(f"""
               | Start Year    | End Year    | Team Name | Drivers in the same Team |
               |---------------|-------------|-----------|--------------------------| 
               |   {first_years_list[0]}   | {last_years_list[0]} | {team_names_list[0]} | {team_mates_list[0]} |  
               |   {first_years_list[1]}   | {last_years_list[1]} | {team_names_list[1]} | {team_mates_list[1]} |     
               |   {first_years_list[2]}   | {last_years_list[2]} | {team_names_list[2]} | {team_mates_list[2]} |     
               |   {first_years_list[3]}   | {last_years_list[3]} | {team_names_list[3]} | {team_mates_list[3]} |
          """)
     elif len(df) == 5:
          st.write(f"""
               | Start Year    | End Year    | Team Name | Drivers in the same Team |
               |---------------|-------------|-----------|--------------------------| 
               |   {first_years_list[0]}   | {last_years_list[0]} | {team_names_list[0]} | {team_mates_list[0]} |  
               |   {first_years_list[1]}   | {last_years_list[1]} | {team_names_list[1]} | {team_mates_list[1]} |     
               |   {first_years_list[2]}   | {last_years_list[2]} | {team_names_list[2]} | {team_mates_list[2]} |     
               |   {first_years_list[3]}   | {last_years_list[3]} | {team_names_list[3]} | {team_mates_list[3]} |    
               |   {first_years_list[4]}   | {last_years_list[4]} | {team_names_list[4]} | {team_mates_list[4]} |
          """)
     elif len(df) == 6:
          st.write(f"""
               | Start Year    | End Year    | Team Name | Drivers in the same Team |
               |---------------|-------------|-----------|--------------------------| 
               |   {first_years_list[0]}   | {last_years_list[0]} | {team_names_list[0]} | {team_mates_list[0]} |  
               |   {first_years_list[1]}   | {last_years_list[1]} | {team_names_list[1]} | {team_mates_list[1]} |     
               |   {first_years_list[2]}   | {last_years_list[2]} | {team_names_list[2]} | {team_mates_list[2]} |     
               |   {first_years_list[3]}   | {last_years_list[3]} | {team_names_list[3]} | {team_mates_list[3]} |    
               |   {first_years_list[4]}   | {last_years_list[4]} | {team_names_list[4]} | {team_mates_list[4]} |    
               |   {first_years_list[5]}   | {last_years_list[5]} | {team_names_list[5]} | {team_mates_list[5]} |   
          """)
     elif len(df) == 7:
          st.write(f"""
               | Start Year    | End Year    | Team Name | Drivers in the same Team |
               |---------------|-------------|-----------|--------------------------| 
               |   {first_years_list[0]}   | {last_years_list[0]} | {team_names_list[0]} | {team_mates_list[0]} |  
               |   {first_years_list[1]}   | {last_years_list[1]} | {team_names_list[1]} | {team_mates_list[1]} |     
               |   {first_years_list[2]}   | {last_years_list[2]} | {team_names_list[2]} | {team_mates_list[2]} |     
               |   {first_years_list[3]}   | {last_years_list[3]} | {team_names_list[3]} | {team_mates_list[3]} |    
               |   {first_years_list[4]}   | {last_years_list[4]} | {team_names_list[4]} | {team_mates_list[4]} |    
               |   {first_years_list[5]}   | {last_years_list[5]} | {team_names_list[5]} | {team_mates_list[5]} |   
               |   {first_years_list[6]}   | {last_years_list[6]} | {team_names_list[6]} | {team_mates_list[6]} | 
          """)     
     else:
          st.write("Too many teams to display!")


def give_spacing(number_lines):
     
     for i in range(0, number_lines):
          st.write(" ")
