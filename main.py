import pandas as pd

flights_2018 = pd.read_csv('delay_2018.csv')
flights_2019= pd.read_csv('delay_2019.csv')


df = pd.concat([flights_2018, flights_2019], ignore_index=True)

print('Number of Rows: ' + str(len(flights_2018)+len(flights_2019)))

df['date'] = pd.to_datetime(df['date'], format='%Y-%m').dt.strftime('%Y-%m')

df = df[(df['date'] >= '2018-01') & (df['date'] <= '2019-12') & (df['arr_flights'].notnull())
              & (df['carrier'].notnull()) & (df['carrier_name'].notnull()) 
              & (df['airport'].notnull()) & (df['airport_name'].notnull())]

print('Number of Rows: ' + str(len(df)))

df['TN'] = df['airport_name'].apply(lambda x: x.find('TN'))
df['NY'] = df['airport_name'].apply(lambda x: x.find('NY'))

airports_TN = set(df[df['TN'] != -1]['airport_name'])
airports_NY = set(df[df['NY'] != -1]['airport_name'])

print('Tennessee Airports:')
print(airports_TN)
print(airports_NY)

flight_coords = pd.read_csv('coords.csv')

flight_airports = df[['airport', 'airport_name']].drop_duplicates().reset_index(drop=True)

df_airports = pd.merge(flight_airports, flight_coords, on='airport')

pd.crosstab(df['carrier'], df['airport'], values=df['arr_diverted'], aggfunc='sum').fillna('')
flights_f = df[(df['date'] >= '2019-01') & (df['date'] <= '2019-12') & (df['airport'] == 'JFK') 
          & (df['carrier_ct'] > 0) & (df['weather_ct'] > 0)]


print("Number of Delays: " + str(flights_f['carrier_ct'].sum()  + flights_f['weather_ct'].sum()))


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
                                    
