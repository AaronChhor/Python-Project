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

print(df.values)


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
    
if Avg_Spirit_count>0:
  Avg_Spirit_del/=Avg_Spirit_count
  print(Avg_Spirit_del)



#print(df.keys)
#spirit_airlines = 0
#for x in df:
#        spirit_airlines = spirit_airlines+1
#     print("Number of Spirit Airlines airports: " + #spirit_airlines)
#print(spirit_airlines)










