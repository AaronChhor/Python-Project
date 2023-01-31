import requests
import json
import pandas as pd

url data = '@opensky-network.org/api/states/all?'
response = requests.get(url_data).json()

name = ['icao24','callsign','origin_country','time_position','last_contact','long','lat','baro_altitude','on_ground','velocity',     'true_track','vertical_rate','sensors','geo_altitude','squawk','spi','position_source']
flight_df=pd.DataFrame(response['states'])
flight_df=flight_df.loc[:,0:16]
flight_df.columns=name
flight_df=flight_df.fillna('No Data')
flight_df.head()