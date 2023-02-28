import pandas as pd

# Read the files and import all rows.
df_18 = pd.read_csv('delays_2018.csv')
#df_19 = pd.read_csv('delays_2019.csv')

# Concatenate the 2018 and 2019 data into a single DataFrame.
df = pd.concat([df_18,], ignore_index=True)

# Print out the number of rows imported from the files.
print('Number of Rows: ' + str(len(df_18)))

# Change the data type of the 'month' column to date and change the format to YYYY-M (e.g. 2018-1).
df['date'] = pd.to_datetime(df['date'], format='%Y-%m').dt.strftime('%Y-%m')

# Remove rows containing invalid data.
df = df[(df['date'] >= '2018-01') & (df['date'] <= '2019-12') & (df['arr_flights'].notnull())
              & (df['carrier'].notnull()) & (df['carrier_name'].notnull()) 
              & (df['airport'].notnull()) & (df['airport_name'].notnull())]

# Print out the number of rows remaining in the dataset.
print('Number of Rows: ' + str(len(df)))

# Identify the airports in the state of Tennessee.
df['TN'] = df['airport_name'].apply(lambda x: x.find('TN'))

# Create a set of airport names (to eliminate the duplicates).
airports = set(df[df['TN'] != -1]['airport_name'])

# Display the list of airports.
print('Tennessee Airports:')
print(airports)

# Read the coordinates file and import all rows.
df_coords = pd.read_csv('airport_coordinates.csv')

# Create a new DataFrame with airport codes and names.
df_airports = df[['airport', 'airport_name']].drop_duplicates().reset_index(drop=True)

# Merge the coordinates DataFrame with the airports DataFrame.
df_airports = pd.merge(df_airports, df_coords, on='airport')

# This code was required due to an Anaconda issue.  You may not need it depending on your environment.
import os
os.environ["PROJ_LIB"] = "C:\\Users\\Nick\\anaconda3\\envs\\sandbox\\Library\\share\\basemap";

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Ready the Basemap for display.
fig = plt.figure(figsize=(16, 16))
m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=32,lat_2=45,lon_0=-95)

# Load the shapefile to display the outlines of the US states.
m.readshapefile('st99_d00', name='states', drawbounds=True)

# Plot the airports on the map.
m.scatter(df_airports['long'].values, df_airports['lat'].values, latlon=True)
plt.show()

#response = requests.get("airport-info.p.rapidapi.com")
#planes = response.json()
#print(response.text)

#requests.get("https://samples.adsbexchange.com/traces/2022/05/01/00/")
#print(response.text)

#urldata = 'https://'+username+':'+password+'@opensky-network.org/api/states/all?'+'lamin='+str(latmin)+'&lomin='+str(longmin)+'&lamax='+str(latmax)+'&lomax='+str(longmax)
#response = requests.get(urldata).json()


#flight_df=pd.DataFrame(response['states'])
#flight_df=flight_df.loc[:,0:16]
#flight_df.columns=name
#flight_df=flight_df.fillna('No Data')
#flight_df.head()



#def flight_tracking(doc):
    
#    flight_source = ColumnDataSource({
 #      'time_position':[],'last_contact':[],'long':[],'lat':[],
  #      'baro_altitude':[],'on_ground':[],'velocity':[],'true_track':[],
   #     'vertical_rate':[],'sensors':[],'geo_altitude':[],'squawk':[],'spi':[],'position_source':[],'x':[],'y':[],
    #    'rot_angle':[],'url':[]
      
    #}
     #                               )      
#origin_country = 'origin_country'
 #Country = input("Countryname: ")
  
#US_planes = int(0)
#for i in response:
#  if i == "United States":
#    US_planes+=1
  
#print(US_planes)

#for i in flight_source:
 # print(time_position)


#print(response)


#country = origin_country
#for i in (response):
#  country = i
                                    
