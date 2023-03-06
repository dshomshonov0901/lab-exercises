#!/usr/bin/env python
# coding: utf-8

# In[41]:


from bs4 import BeautifulSoup
import requests
import html5lib
import csv
import pandas as pd

source=requests.get("https://www.imdb.com/list/ls055592025/").text
soup=BeautifulSoup(source, "lxml")
print(soup)
##Isolate the title, the date of release, and one other element of your choosing (for all 100). (3pts) Put the data into a csv. (2pts)#


# In[40]:


csv_file = open("cms_imbd.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Title", "Rating", "Release Date"]) #, "date of release", "rating"/#

for element in soup.find_all("div", class_="lister-item-content"):
    
    title=element.find("a").text.strip()
    print(title)
    rating=element.find("span", class_="ipl-rating-star__rating").text.strip()
    print(rating)
    date=element.find("span", class_="lister-item-year text-muted unbold").text.strip("()")
    print(date)
    
    
    
    csv_writer.writerow([title, rating, date])#, date, rating/#

csv_file.close()
imbdread=pd.read_csv("cms_imbd.csv")
imbdread

