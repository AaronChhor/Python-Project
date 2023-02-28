import pandas as pd


df_18 = pd.read_csv('delays_2018.csv')
df_19 = pd.read_csv('delays_2019.csv')


df = pd.concat([df_18, df_19], ignore_index=True)

print('Number of Rows: ' + str(len(df_18)+len(df_19)))

df['date'] = pd.to_datetime(df['date'], format='%Y-%m').dt.strftime('%Y-%m')

df = df[(df['date'] >= '2018-01') & (df['date'] <= '2019-12') & (df['arr_flights'].notnull())
              & (df['carrier'].notnull()) & (df['carrier_name'].notnull()) 
              & (df['airport'].notnull()) & (df['airport_name'].notnull())]

print('Number of Rows: ' + str(len(df)))

df['TN'] = df['airport_name'].apply(lambda x: x.find('TN'))

airports = set(df[df['TN'] != -1]['airport_name'])

print('Tennessee Airports:')
print(airports)

df_coords = pd.read_csv('airport_coordinates.csv')

df_airports = df[['airport', 'airport_name']].drop_duplicates().reset_index(drop=True)

df_airports = pd.merge(df_airports, df_coords, on='airport')

pd.crosstab(df['carrier'], df['airport'], values=df['arr_diverted'], aggfunc='sum').fillna('')
df_f = df[(df['date'] >= '2019-01') & (df['date'] <= '2019-12') & (df['airport'] == 'JFK') 
          & (df['carrier_ct'] > 0) & (df['weather_ct'] > 0)]


print("Number of Delays: " + str(df_f['carrier_ct'].sum()  + df_f['weather_ct'].sum()))


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
                                    
