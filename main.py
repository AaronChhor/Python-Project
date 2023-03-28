import pandas as pd

df = pd.read_csv('airline_delay_causes.csv')
#df.head(3)
#df["arr_delay"].head()
Spirit_df= df[ df['region']=="Spirit Air Lines"]
Spirit_df.head()
Spirit_df.index
Spirit_df.set_index("Year", inplace=True)
Spirit_df.plot()


print('Number of Rows: ' + str(len(df)))
Rows=int(str(len(df)))

df['year'] = pd.to_datetime(df['year'], format='%Y-%m').dt.strftime('%Y-%m')

df = df[(df['year'] >= '2016') & (df['arr_flights'].notnull())
              & (df['carrier'].notnull()) & (df['carrier_name'].notnull()) 
              & (df['airport'].notnull()) & (df['airport_name'].notnull())]

#print('Number of Rows: ' + str(len(df)))

print(df.values)
#print(df.keys)
#spirit_airlines = 0
#for x in df:
#        spirit_airlines = spirit_airlines+1
#     print("Number of Spirit Airlines airports: " + #spirit_airlines)
#print(spirit_airlines)

#for i in df.keys():
key = "Spirit Air Lines"
Spirit_airlines = 0
for i in df.values:
  if i == key:
    Spirit_airlines+=1
print(Spirit_airlines)

Spirit_avg = Spirit_airlines/Rows

#Find Average minutes of delay
key = 'Spirit Air Lines'
Avg_Spirit_del = 0
Avg_Spirit_count = 0
for i in df.values:
  if i == key:
    Avg_Spirit_del+= 'arr_delay'
    Avg_Spirit_count+=1
    
#if Avg_Spirit_count>0:
#  Avg_Spirit_del/=Avg_Spirit_count
#  print(Avg_Spirit_del)


    

#print("Number of Delays: " + str(flights_f['carrier_ct'].sum()  + flights_f['weather_ct'].sum()))










#df['TN'] = df['airport_name'].apply(lambda x: x.find('TN'))
#df['NY'] = df['airport_name'].apply(lambda x: x.find('NY'))

#airports_TN = set(df[df['TN'] != -1]['airport_name'])
#airports_NY = set(df[df['NY'] != -1]['airport_name'])

#print('Tennessee Airports:')
#print(airports_TN)
#print(airports_NY)

#flight_coords = pd.read_csv('coords.csv')

#flight_airports = df[['airport', 'airport_name']].drop_duplicates().reset_index(drop=True)

#df_airports = pd.merge(flight_airports, flight_coords, on='airport')

#pd.crosstab(df['carrier'], df['airport'], values=df['arr_diverted'], aggfunc='sum').fillna('')
#flights_f = df[(df['date'] >= '2019-01') & (df['date'] <= '2019-12') & (df['airport'] == 'JFK') 
        #  & (df['carrier_ct'] > 0) & (df['weather_ct'] > 0)]





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
                                    
