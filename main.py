import pandas as pd

df = pd.read_csv('airline_delay_causes.csv')
#df.head(3)
#df["arr_delay"].head()
#Spirit_df= df[ df['airport_name']=='Spirit Air Lines']
#Spirit_df.head()
#Spirit_df.index
#Spirit_df.set_index('arr_delay', inplace=True)
#Spirit_df.plot()

print (df.shape)
print (df.columns)
print (df.head(n=5))
print (df[["airport_name", "carrier"]].head(n=10))
print ("xxx")


print('Number of Rows: ' + str(len(df)))
Rows=int(str(len(df)))

df['year'] = pd.to_datetime(df['year'], format='%Y-%m').dt.strftime('%Y-%m')

df = df[(df['year'] >= '2016') & (df['arr_flights'].notnull())
              & (df['carrier'].notnull()) & (df['carrier_name'].notnull()) 
              & (df['airport'].notnull()) & (df['airport_name'].notnull())]

print(df.values)


Avg_Spirit_count = 0

with open('airline_delay_causes.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if "Spirit Air Lines" in line:
            Avg_Spirit_count += 1

print("Number of occurrences of 'Spirit Air Lines':", Avg_Spirit_count)

if Avg_Spirit_count>0:
  Avg_Spirit_count/=Rows
  print("Percentage of flights made by 'Spirit Air Lines':", Avg_Spirit_count*100, "%")




#for i in df.keys():
#key = "Spirit Air Lines"
#Spirit_airlines = 0
#for i in df.values:
#  if i == key:
#    Spirit_airlines+=1
#print(Spirit_airlines)

#Spirit_avg = Spirit_airlines/Rows

#Find Average minutes of delay
key = 'Spirit Air Lines'
Avg_Spirit_del = 0
Avg_Spirit_count = 0
for i in df.values:
  if i == key:
    Avg_Spirit_del+= 'arr_delay'
    Avg_Spirit_count+=1
    




#print(df.keys)
#spirit_airlines = 0
#for x in df:
#        spirit_airlines = spirit_airlines+1
#     print("Number of Spirit Airlines airports: " + #spirit_airlines)
#print(spirit_airlines)










