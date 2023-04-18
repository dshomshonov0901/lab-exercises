#!/usr/bin/env python
# coding: utf-8

# In[26]:


from tkinter import *
import requests
from PIL import Image,ImageTk

def get_forecast():
    lat = lat_entry.get()
    lon = lon_entry.get()
    location_url = f"https://api.weather.gov/points/{lat},{lon}"
    r = requests.get(location_url).json()
    forecast_url = r['properties']['forecast']
    forecast_response = requests.get(forecast_url).json()
    forecast_data = forecast_response['properties']['periods']

    forecast_label.config(text=f"7-day Forecast for latitude {lat}, longitude {lon}:")

    for i in range(7):
        date = forecast_data[i]['name']
        temp = forecast_data[i]['temperature']
        desc = forecast_data[i]['shortForecast']
        day_frame = Frame(root, bd=1, relief=RIDGE)
        day_frame.pack(pady=5, padx=10)
        date_label = Label(day_frame, text=date)
        date_label.pack(side=LEFT, padx=5)
        temp_label = Label(day_frame, text=f"{temp}\N{DEGREE SIGN}F")
        temp_label.pack(side=LEFT, padx=20)
        desc_label = Label(day_frame, text=desc)
        desc_label.pack(side=LEFT)

root = Tk()
root.title("7-Day Forecast")
root.geometry("600x500")


#This was my attempt at using the Canvas widget but the code wasn't working
#C = Canvas(root, bg="blue", height=250, width=300)
#C.pack()
#img = ImageTk.PhotoImage(Image.open("weather_globe.jpg"))
#C.create_image(10,10,anchor=NW,image=img)

lat_label = Label(root, text="Latitude:")
lat_label.pack(pady=5)
lat_entry = Entry(root)
lat_entry.pack()

lon_label = Label(root, text="Longitude:")
lon_label.pack(pady=5)
lon_entry = Entry(root)
lon_entry.pack()

get_forecast_button = Button(root, text="Get Forecast", command=get_forecast)
get_forecast_button.pack(pady=10)

forecast_label = Label(root, text="")
forecast_label.pack()

root.mainloop()


# In[ ]:




