import requests
import json
import pandas as pd
import http.client
#pd.read_json('@opensky-network.org/api/states/all')


conn = http.client.HTTPSConnection("airport-info.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "5a89e79fe4msh7410d61b0054b56p1bff01jsn662d1919dcf9",
    'X-RapidAPI-Host': "airport-info.p.rapidapi.com"
    }

conn.request("GET", "/airport?iata=JFK&icao=KJFK", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

#response = requests.get("airport-info.p.rapidapi.com")
#planes = response.json()
#print(response.text)

#requests.get("https://samples.adsbexchange.com/traces/2022/05/01/00/")
#print(response.text)

#urldata = 'https://'+username+':'+password+'@opensky-network.org/api/states/all?'+'lamin='+str(latmin)+'&lomin='+str(longmin)+'&lamax='+str(latmax)+'&lomax='+str(longmax)
#response = requests.get(urldata).json()

name = ['icao24','callsign','origin_country','time_position','last_contact','long','lat','baro_altitude','on_ground','velocity',     'true_track','vertical_rate','sensors','geo_altitude','squawk','spi','position_source']

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
                                    
