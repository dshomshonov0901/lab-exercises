#!/usr/bin/env python
# coding: utf-8

# In[147]:


import requests
import json
import csv

lat = "40.615360"
lon = "-74.005840"

genius = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

json_file=genius.json()
json_file


# In[150]:


forecast = json_file["properties"]["forecast"]
new_request = requests.get(forecast)
json = new_request.json()
json


# In[13]:


import csv
csv_file = open("weather.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Day", "Temp", "Description"])
specific = json["properties"]["periods"]
for r in range(0, len(specific)):
    name = specific[r]['name']
    temperature = str(specific[r]['temperature']) +  specific[r]['temperatureUnit']
    detailed = specific[r]['detailedForecast']
    print(specific[r]['name'])
    print(str(specific[r]['temperature']) +  specific[r]['temperatureUnit'])
    print(specific[r]['detailedForecast'])
    r+=1
    
    csv_writer.writerow([name, temperature, detailed])

csv_file.close()


# In[34]:


import pandas as pd
sheet = pd.read_csv("weather.csv")
sheet = sheet.sort_values(by="Temp", ascending = True)
sheet


# In[42]:


from matplotlib import pyplot as plt
import numpy as np

df=pd.DataFrame(sheet)

day = df["Day"]
temp = df["Temp"]

fig = plt.figure(figsize = (25,10))
plt.bar(day[0:14], temp[0:14])
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Temperatures on Days")


plt.show()


# In[111]:


Year = 2022
CountryCode=["AT", "AL", "AF", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG"]
i=0
api = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/{Year}/{CountryCode[i]}")

json_file=api.json()
json_file


# In[ ]:


#/api/v3/CountryInfo/{countryCode} gives the common name, official name, country code, region, and borders given a country code
#/api/v3/AvailableCountries simply gives all the available countries as a country code and name 
#/api/v3/LongWeekend/{year}/{countryCode} takes parameters year and country code and responds with the start and end date of long weekends in the country as well as how long the weekend was and if a bridge day was needed
#/api/v3/PublicHolidays/{year}/{countryCode} takes parameters year and country code and responds with the date, local and regular name of the holiday, as well as the country code, whether the holiday is fixed and global. It also returns which counties it is celebrated in , the launch year and the type of holiday.
#/api/v3/IsTodayPublicHoliday/{countryCode} takes parameter of country code and responds with whether today is a public holiday in the given country
#/api/v3/NextPublicHolidays/{countryCode} takes parameter country code and returns the upcoming public holidays for the next 365 days for the given country. It returns the same variables that the Public Holidays API does
#/api/v3/NextPublicHolidays/{countryCode} takes no parameters and returns the upcoming public holidays for the next 7 days worldwide.


# In[ ]:


CountryCodes=["AT", "AL", "IT", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG"]
CountryCode= ''.join(random.sample(CountryCodes, 1)


# In[143]:


import random
import json
import requests
CountryCodes=["AT", "AL", "IT", "CL", "CN", "AD", "JE", "MD", "PE", "RS"]
number_of_holidays =[]
i=0
csv_file = open("holidays.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Country Code", "Number of Holidays"])
for i in range(0,10):
    CountryCode=CountryCodes[i]
    holiday= requests.get(f"https://date.nager.at/api/v3/NextPublicHolidays/{CountryCode}")
    json_file=holiday.json()
    code = json_file[0]['countryCode']
    length = len(json_file)
    number_of_holidays.append(length)
    i+=1
    csv_writer.writerow([code, length])

csv_file.close()
    
print(number_of_holidays)
    


# In[144]:


import pandas as pd
sheet2 = pd.read_csv("holidays.csv")
sheet2


# In[145]:


from matplotlib import pyplot as plt
import numpy as np

df=pd.DataFrame(sheet2)

code = df["Country Code"]
length= df["Number of Holidays"]

fig = plt.figure(figsize = (25,10))
plt.bar(code[0:14], length[0:14])
plt.xlabel("Country Code")
plt.ylabel("Number of Holidays")
plt.title("Number of Holidays for 10 countries")


plt.show()

