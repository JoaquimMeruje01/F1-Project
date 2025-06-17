import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px


def app():

    st.title("Circuits")

    st.write("In Drivers and Teams you can discover more about your favourite drivers and teams. Since simple stats about championships, number of points or wins, until more complex statistics over the years.")

    init_stats_circuits()
    give_spacing(2)
    drivers_teams_performance_circuits()


def init_stats_circuits():

    st.markdown("### Circuits Statistics")

    df_final_circuits = pd.read_csv(r"C:\Users\Joaquim Meruje\OneDrive\Documentos\F1 Project\Web App\dataframes\circuits_final.csv")
    col1, col2 = st.columns([0.5, 0.5])

    with col1:
        drivers_name = df_final_circuits["driverName"].unique().tolist()
        drivers_name.sort()
        drivers_name.insert(0, "All") 
        driver_selected = st.selectbox("Driver Name", drivers_name)
        if driver_selected != "All":
            df_final_circuits = df_final_circuits[df_final_circuits['driverName'] == driver_selected]   

    with col2:
        country_name = df_final_circuits["country"].unique().tolist()
        country_name.sort()
        country_name.insert(0, "All")  
        country_selected = st.selectbox("Country", country_name) 
        if country_selected != "All":
            df_final_circuits = df_final_circuits[df_final_circuits['country'] == country_selected]     

    df_final_circuits = df_final_circuits.drop(columns=['circuitId'])
    df_final_circuits.rename(columns={'name': 'Circuit Name',
                                      'location': 'Location',
                                      'country': 'Country',
                                      'num_races': 'Races',
                                      'driverName': 'Driver Name',
                                      'fastestLapTime': 'Fast Lap Time'
                                    }, inplace=True)
    df_final_circuits = df_final_circuits.sort_values(by=['Races'], ascending=False).head(10)
    df_final_circuits.index = range(1, len(df_final_circuits) + 1)
    st.dataframe(df_final_circuits)


def drivers_teams_performance_circuits():

     st.markdown("### Drivers and Teams Performance in Circuits")

     results_by_circuit = pd.read_csv(r"C:\Users\Joaquim Meruje\OneDrive\Documentos\F1 Project\Web App\dataframes\results_by_circuit.csv ") 
     col1, col2 = st.columns([0.4, 0.4])

     with col1:
          list_country = results_by_circuit["country"].unique().tolist()
          list_country.sort()
          country_selected = st.selectbox("Country", list_country, index=12)

     with col2:
          min_year = int(results_by_circuit['year'].min())
          max_year = int(results_by_circuit['year'].max())
          start_year, end_year = st.slider("Years Interval", min_value=min_year, max_value=max_year, value=(min_year, max_year))

     results_by_circuit = results_by_circuit[(results_by_circuit['country'] == country_selected) &
                                            (results_by_circuit['year'] >= start_year) & (results_by_circuit['year'] <= end_year)]     

     list_circuits = sorted(results_by_circuit["Circuit Name"].unique().tolist())
     selected_circuit = list_circuits[0]

     if len(list_circuits) == 1:
          if col1.button(list_circuits[0]):
               selected_circuit = list_circuits[0]

     elif len(list_circuits) == 2:
          colZ, colY = st.columns([0.5, 0.5])
          if colZ.button(list_circuits[0]):
               selected_circuit = list_circuits[0]
          if colY.button(list_circuits[1]):
               selected_circuit = list_circuits[1]

     elif len(list_circuits) == 3:
          colZ, colY, colX = st.columns([0.33, 0.33, 0.33])
          if colZ.button(list_circuits[0]):
               selected_circuit = list_circuits[0]
          if colY.button(list_circuits[1]):
               selected_circuit = list_circuits[1]
          if colX.button(list_circuits[2]):
               selected_circuit = list_circuits[2]

     elif len(list_circuits) >= 4:
          colZ, colY, colX, colW = st.columns([0.25, 0.25, 0.25, 0.25])
          if colZ.button(list_circuits[0]):
               selected_circuit = list_circuits[0]
          if colY.button(list_circuits[1]):
               selected_circuit = list_circuits[1]
          if colX.button(list_circuits[2]):
               selected_circuit = list_circuits[2]
          if colW.button(list_circuits[3]):
               selected_circuit = list_circuits[3]

     medium_velocity_over_the_years(selected_circuit, results_by_circuit)
     drivers_teams_race_status(selected_circuit, results_by_circuit)


def medium_velocity_over_the_years(selected_circuit, results_by_circuit):

     st.markdown("##### Medium Velocity Over the Years")

     results_by_circuit = results_by_circuit[results_by_circuit['Circuit Name'] == selected_circuit]
     results_by_circuit = results_by_circuit.rename(columns={
          'fastestLapTime_mean': 'Fastest Lap Time',
          'fastestLapSpeed_mean': 'Fastest Lap Speed',
          'milliseconds': 'Racing Time',
          'year': 'Years'
     })

     results_by_circuit = results_by_circuit.dropna()
     results_by_circuit = results_by_circuit.sort_values(by='Years')

     columns_all = ['Fastest Lap Time',	'Fastest Lap Speed', 'Racing Time']
     columns_to_plot = st.selectbox('Options', columns_all, index=0)

     print(f'Columns to plot: {columns_to_plot}')

     fig = px.line(results_by_circuit,
                    x="Years",
                    y=columns_to_plot)

     st.plotly_chart(fig)


def drivers_teams_race_status(selected_circuit, results_by_circuit):
    
    col1, col2 = st.columns(2)

    filtered = results_by_circuit[results_by_circuit['Circuit Name'] == selected_circuit]

    # Drivers Pie Chart 
    circuit_driver_winner = (
        filtered.groupby(['driverName'])
        .size()
        .reset_index(name='Wins')
        .sort_values(by='Wins', ascending=False)
    )

    with col1:
        st.markdown("##### Drivers Best Performances")
        pie_drivers = alt.Chart(circuit_driver_winner).mark_arc(innerRadius=50, outerRadius=120).encode(
            theta=alt.Theta(field='Wins', type='quantitative'),
            color=alt.Color(field='driverName', type='nominal', legend=None),
            tooltip=[
                alt.Tooltip('driverName:N', title='Driver Name'),
                alt.Tooltip('Wins:Q', title='Wins')
            ],
            order=alt.Order('Wins:Q', sort='descending')  # <- Isto garante a ordem no desenho
        ).properties(width=400, height=400).configure(background='#15151D')

        st.altair_chart(pie_drivers)

    # Teams Pie Chart
    circuit_team_winner = (
        filtered.groupby(['Team Name'])
        .size()
        .reset_index(name='Wins')
        .sort_values(by='Wins', ascending=False)
    )

    with col2:
        st.markdown("##### Teams Best Performances")
        pie_teams = alt.Chart(circuit_team_winner).mark_arc(innerRadius=50, outerRadius=120).encode(
            theta=alt.Theta(field='Wins', type='quantitative'),
            color=alt.Color(field='Team Name', type='nominal', legend=None),
            tooltip=[
                alt.Tooltip('Team Name:N', title='Team Name'),
                alt.Tooltip('Wins:Q', title='Wins')
            ],
            order=alt.Order('Wins:Q', sort='descending')  # <- Ordenação das fatias
        ).properties(width=400, height=400).configure(background='#15151D')

        st.altair_chart(pie_teams)


def give_spacing(number_lines):
     
     for i in range(0, number_lines):
          st.write(" ")
          
     
