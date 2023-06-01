import pandas as pd
import csv
import matplotlib.pyplot as plt

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


#Find Average minutes of delay
key = 'Spirit Air Lines'
Avg_Spirit_del = 0
Avg_Spirit_count = 0
for i in df.values:
  if i == key:
    Avg_Spirit_del+= 'arr_delay'
    Avg_Spirit_count+=1


delay_dict = {}
ontime_dict = {}

with open('airline_delay_causes.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        brand = row[3]  
        airport = row[5]  
        delay = 0
        try:
            delay = int(float(row[7]))
        except ValueError:
            #ignores rows with string in column 6
            continue
        
        if brand not in delay_dict:
            delay_dict[brand] = {airport: [delay, 1]}  
        else:
            if airport not in delay_dict[brand]:
                delay_dict[brand][airport] = [delay, 1]  
            else:
                delay_dict[brand][airport][0] += delay  
                delay_dict[brand][airport][1] += 1  

for brand in delay_dict:
    print(brand)
    for airport in delay_dict[brand]:
        avg_delay = delay_dict[brand][airport][0] / delay_dict[brand][airport][1]
        print(f'{airport}: {avg_delay:.2f} delays') #Average delays over all 10 years which explains the decimal

#Finds the amount of flights by each company

filename = "airline_delay_causes.csv"

airport_counts = {}

with open(filename, "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  
    for row in reader:
        airport_name = row[5]
        if airport_name in airport_counts:
            airport_counts[airport_name] += 1
        else:
            airport_counts[airport_name] = 1

print("\n".join([f"{airport},{count}" for airport, count in airport_counts.items()]))

delay_dict = {}
airport_counts = {}  # Initialize the dictionary before using it

with open('airline_delay_causes.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        brand = row[3]  
        airport = row[5]  
        delay = 0
        try:
            delay = int(float(row[7]))
        except ValueError:
            continue
        
        if brand not in delay_dict:
            delay_dict[brand] = {airport: [delay, 1]}  
        else:
            if airport not in delay_dict[brand]:
                delay_dict[brand][airport] = [delay, 1]  
            else:
                delay_dict[brand][airport][0] += delay  
                delay_dict[brand][airport][1] += 1
         
        if airport in airport_counts:
            airport_counts[airport] += 1
        else:
            airport_counts[airport] = 1

delay_scores = {}  # Dictionary to store delay scores for each airport

for brand in delay_dict:
    for airport in delay_dict[brand]:
        avg_delay = delay_dict[brand][airport][0] / delay_dict[brand][airport][1]
        flight_count = airport_counts.get(airport, 0)
        total_delay = avg_delay * flight_count
        total_delay = total_delay / len(delay_dict)  # Divide by the number of rows in the dataset
        delay_scores[airport] = total_delay

ranked_airports = sorted(delay_scores, key=delay_scores.get, reverse=True)

for rank, airport in enumerate(ranked_airports, start=1):
    delay_score = delay_scores[airport]/Rows
    print(f'Rank {rank}: {airport} - Delay Score: {delay_score:.2f}')

#Graphs


# Plotting the ranks
ranks = range(1, len(ranked_airports) + 1)
delay_scores_normalized = [delay_scores[airport] / Rows for airport in ranked_airports]
plt.bar(ranks, delay_scores_normalized)
plt.xlabel('Rank')
plt.ylabel('Delay Score (Normalized)')
plt.title('Airport Delay Rankings')
plt.show()

#Multiplies the amount of delays by percentage of flights made while adding 1



#for i in delay_dict:
#  delay_dict[i]/Rows
#print (delay_dict)



#print(df.keys)
#spirit_airlines = 0
#for x in df:
#        spirit_airlines = spirit_airlines+1
#     print("Number of Spirit Airlines airports: " + #spirit_airlines)
#print(spirit_airlines)










