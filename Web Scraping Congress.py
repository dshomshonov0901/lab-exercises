#!/usr/bin/env python
# coding: utf-8

# In[74]:


from bs4 import BeautifulSoup
import requests
import html5lib
import csv
source=requests.get("https://www.loc.gov/search/?q=cats&sp=1").text
soup=BeautifulSoup(source, "lxml")
print(soup)
##Scrape the first 5 pages, grab the title, item description, and webpage hyperlink. (3pts) Put the data into a csv. (2pts)



# In[76]:


section = soup.find("div", class_="item-description")
print(section.prettify())


# In[ ]:


csv_file = open("cms_congress.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Title", "Description", "Link"]) #, "description","link", "contributer name", "date"/#
page = 1
while page !=6:
    source=requests.get(f"https://www.loc.gov/search/?q=cats&sp={page}").text
    soup=BeautifulSoup(source, "lxml")
    for element in soup.find_all("div", class_="item-description"):
    
        title=element.span.a.text.strip()
        print(title)
         
        if element.find("span", class_ = "item-description-abstract") == None:
            description="not given"
            print(description)
        else:
            description = element.find("span", class_="item-description-abstract").text.strip()
            print(description)
        
        link = element.span.a.get("href").strip()
        print(link)
    
    
        csv_writer.writerow([title, description, link])#, date, rating/#
        page+=1

    
csv_file.close()

catsread=pd.read_csv("cms_congress.csv")
catsread


# In[ ]:





# In[ ]:




