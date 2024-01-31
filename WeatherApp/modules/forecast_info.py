#                                                                                  #
import modules.settings as set
import customtkinter as ctk
import modules.api_call as api
import datetime
from PIL import Image
import os
PATH = os.path.abspath(__file__ + "/../../images/icon")


class Forecast:
    def __init__(self, master, weather, temp, time, real_time):
        self.master = master
        self.time = time
        self.wheather = weather
        self.temp = temp
        self.real_time = real_time
        self.image = set.find_image(weather = self.wheather, time = self.real_time)
        self.create_label()
        
  
    def create_label(self):
        self.frame = ctk.CTkFrame(
            master = self.master,
            fg_color = "#5DA7B1",
            width = 100,
            height = 400
          )
        time = ctk.CTkLabel(
            master = self.frame,
            # text = f"{int(datetime.datetime.now().strftime('%H')) + self.time}:00",
            text = f"{self.real_time}:00",
            text_color= "#FFFFFF",
            font = set.font(size_font = 20)
        )
        image = ctk.CTkImage(
            dark_image = Image.open(PATH + "/" + self.image),
            size = (50, 50)
        )
        image_label = ctk.CTkLabel(
            master= self.frame,
            text= "",
            image= image,
            width= 90,
            height= 100
        )
        temp_label = ctk.CTkLabel(
            master= self.frame,
            text= f"{round(self.temp) - 273}°",
            text_color= "#FFFFFF",
            font = set.font(size_font = 35, bold ="bold") 
        )
        time.grid(row = 0)
        image_label.grid(row = 1)
        temp_label.grid(row = 2)
    
    def place_self(self):
        self.frame.grid(row = 0, column = self.time)


class ForecastInfo:
    def __init__(self, master):
        self.master = master
        self.weather_data = None
        self.time = 0
        self.real_time = int(datetime.datetime.now().strftime('%H'))

    def create_forecast(self):
        self.weather_data = api.get_forecast_data()
        for hour in self.weather_data["list"]:
            
            self.time += 1  
            if self.time + int(datetime.datetime.now().strftime('%H')) < 24:
                self.real_time = int(datetime.datetime.now().strftime('%H')) + self.time
            elif self.time + int(datetime.datetime.now().strftime('%H')) > 24:
                self.real_time = self.time + int(datetime.datetime.now().strftime('%H')) - 24
            elif self.time + int(datetime.datetime.now().strftime('%H')) == 24:
                self.real_time = 0
                
              

            self.forecast = Forecast(
                master = self.master,
                weather = hour["weather"][0]["main"],
                temp = hour["main"]["temp"],
                time = self.time,
                real_time = self.real_time
                
            )
            self.forecast.place_self()
            if self.time > 23:
                break

"""

{
  "cod": "200",
  "message": 0,
  "cnt": 40,
  "list": [
    {
      "dt": 1661871600,
      "main": {
        "temp": 296.76,
        "feels_like": 296.98,
        "temp_min": 296.76,
        "temp_max": 297.87,
        "pressure": 1015,
        "sea_level": 1015,
        "grnd_level": 933,
        "humidity": 69,
        "temp_kf": -1.11
      },
      "weather": [
        {
          "id": 500,
          "main": "Rain",
          "description": "light rain",
          "icon": "10d"
        }
      ],
      "clouds": {
        "all": 100
      },
      "wind": {
        "speed": 0.62,
        "deg": 349,
        "gust": 1.18
      },
      "visibility": 10000,
      "pop": 0.32,
      "rain": {
        "3h": 0.26
      },
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2022-08-30 15:00:00"
    },
 }
"""