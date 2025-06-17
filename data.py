import pandas as pd

# Teams data

redbull = ['Stewart', 'Jaguar', 'Red Bull']
redbull_years = [1997, 2000, 2005]

ferrari = ['Ferrari']
ferrari_years = [1950]

alpine = ['Toleman', 'Benetton', 'Renault', 'Lotus', 'Renault', 'Alpine F1 Team']
alpine_years = [1981, 1986, 2002, 2010, 2016, 2021]

mercedes = ['Tyrrell', 'BAR', 'Honda', 'Brawn', 'Mercedes']
mercedes_years = [1970, 1999, 2006, 2009, 2010]

mclaren = ['McLaren']
mclaren_years = [1966]

rb = ['Minardi', 'Toro Rosso', 'AlphaTauri', 'RB F1 Team']
rb_years = [1985, 2006, 2020, 2024]

sauber = ['Sauber', 'BMW Sauber', 'Sauber', 'Alfa Romeo', 'Sauber']
sauber_years = [1993, 2006, 2010, 2019, 2024]

haas = ['Haas F1 Team']
haas_years = [2016]

aston_martin = ['Jordan', 'MF1', 'Spyker', 'Force India', 'Racing Point', 'Aston Martin']
aston_martin_years = [1991, 2006, 2007, 2008, 2018, 2021]

williams = ['Williams']
williams_years = [1978]

manor= ['Virgin', 'Marussia', 'Manor Marussia']
manor_years = [2010, 2012, 2015]

caterham = ['Lotus', 'Caterham']
caterham_years = [2010, 2012]

hispania = ['HRT']
hispania_years = [2010]

arrows = ['Arrows', 'Footwork']
arrows_years = [1978, 1991]

prost = ['Ligier', 'Prost']
prost_years = [1976, 1997]

toyota = ['Toyota']
toyota_years = [2002]

super_aguri = ['Super Aguri']
super_aguri_years = [2006]


teams_names = ['Red Bull', 'Ferrari', 'Alpine', 'Mercedes', 'Mclaren', 'RB', 'Sauber', 'Haas', 'Aston Martin',
                'Williams', 'Manor', 'Caterham', 'Hispania', 'Arrows', 'Prost', 'Toyota', 'Super Aguri']

teams_lists = [redbull, ferrari, alpine, mercedes, mclaren, rb, sauber, haas, aston_martin, williams, manor,
               caterham, hispania, arrows, prost, toyota, super_aguri]

team_mapping = dict(zip(teams_names, teams_lists))

teams_years_list = [redbull_years, ferrari_years, alpine_years, mercedes_years, mclaren_years, rb_years, sauber_years, haas_years, 
                      aston_martin_years, williams_years, manor_years, caterham_years, hispania_years, arrows_years, prost_years,
                      toyota_years, super_aguri_years]



# Mechanical Problems Data

engine_columns = [
    "Alternator", "Battery", "Cooling system",
    "Crankshaft", "ERS", "Engine", "Engine fire", 
    "Engine misfire", "Magneto", "Overheating",
    "Power Unit", "Power loss", "Radiator", 
    "Spark plugs", "Supercharger", "Turbo"
] 

aerodynamics_columns = [
    "Broken wing", "Chassis", "Front wing", 
    "Rear wing", "Undertray", "Underweight"
]

transmission_columns = [
    "Axle", "CV joint", "Differential", 
    "Driveshaft", "Drivetrain", "Gearbox", 
    "Halfshaft", "Transmission"
]

electronic_systems_columns = [
    "Electrical", "Electronics", "Ignition", "Launch control"
]

mechanical_systems_columns = [
    "Clutch", "Hydraulics", "Mechanical", "Pneumatics"
]

suspension_and_direction_columns = [
    "Handling", "Steering", "Suspension", "Track rod"
]

fuel_columns = [
    "Fuel", "Fuel leak", "Fuel pipe", "Fuel pressure", 
    "Fuel pump", "Fuel rig", "Fuel system", 
    "Out of fuel", "Refuelling"
]

oil_columns = [
    "Oil leak", "Oil line", "Oil pipe", 
    "Oil pressure", "Oil pump"
]

water_columns = [
    "Water leak", "Water pipe", "Water pressure", "Water pump"
]

wheel_columns = [
    "Wheel", "Wheel bearing", "Wheel nut", "Wheel rim"
]

mechanical_parameters = (
    engine_columns +
    aerodynamics_columns +
    transmission_columns +
    electronic_systems_columns +
    mechanical_systems_columns +
    suspension_and_direction_columns +
    fuel_columns +
    oil_columns +
    water_columns +
    wheel_columns
)

mechanical_columns = (
    "engine_columns",
    "aerodynamics_columns",
    "transmission_columns",
    "electronic_systems_columns",
    "mechanical_systems_columns",
    "suspension_and_direction_columns",
    "fuel_columns",
    "oil_columns",
    "water_columns",
    "wheel_columns"
)