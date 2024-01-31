#PARKING 
import os, sqlite3, customtkinter as ctk
import datetime

PATH = os.path.abspath(__file__ + "/../..")   

def font(size_font, underline = False, bold = None, italic = "roman"):
    return ctk.CTkFont(family = f"Roboto Slab Semibold", size = size_font, weight= bold, slant = italic, underline = underline)
        
def get_data(name_data):
    connection_data = sqlite3.connect(PATH + "/data_base/data_base.db")
    cursor = connection_data.cursor()
    cursor.execute(f"SELECT {name_data} FROM user")
    connection_data.commit()
    data = cursor.fetchone()
    connection_data.close()
    return data[0]

def table_not_empty():
    connection_data = sqlite3.connect(PATH + "/data_base/data_base.db")
    cursor = connection_data.cursor()
    cursor.execute(f"SELECT count(*) FROM user")
    connection_data.commit()
    data = cursor.fetchall()
    connection_data.close()
    return data[0][0]


def database_command(string):
    connection_data = sqlite3.connect(PATH + "/data_base/data_base.db")
    cursor = connection_data.cursor()
    cursor.execute(string)
    connection_data.commit()
    connection_data.close()

weekdays = ["Понеділок","Вівторок","Середа","Четвер","П'ятниця", "Субота", "Неділя"]

list_date = []

def get_date_info():
    global list_date
    list_date = []
    weekday_i = datetime.date.today().weekday()
    list_date.append(weekdays[weekday_i])
    list_date.append(datetime.datetime.now().strftime('%d.%m.%y'))
    list_date.append(datetime.datetime.now().strftime('%H:%M'))
get_date_info()

weather_images = {
    "day": {
        "Clear": "sun.png",
        "Clouds": "clouds_d.png",
        "Rain": "rain_d.png",
        "Thunder": "storm.png",
        "Snow": "snowy_d.png",
        "Drizzle": "drizzle_d.png",
        "Mist": "drizzle_d.png",
        "Haze": "drizzle_d.png",
        "Fog": "drizzle_d.png"
    },
    "night": {
        "Clear": "moon.png",
        "Clouds": "clouds_n.png",
        "Rain": "rain_n.png",
        "Thunder": "storm.png",
        "Snow": "snowy_n.png",
        "Drizzle": "drizzle_n.png",
        "Mist": "drizzle_n.png",
        "Haze": "drizzle_n.png",
        "Fog": "drizzle_n.png"
    }
}

def find_image(weather = None, time = int(datetime.datetime.now().strftime('%H'))):
    if 6 < time < 22:
        daytime = "day"
    else:
        daytime = "night"  

    # if weather == None:
        # json = api.get_city_data(city= get_data('city'))
        # weather = json["weather"][0]["main"]
        
    try:    
        return weather_images[daytime][weather["weather"][0]["main"]]
    except:
        if daytime == "day":
            return "clouds_d.png"
        else:
            return "clouds_n.png"
        
def update_time(label):
    label.configure(text = f"{datetime.datetime.now().strftime('%H:%M')}")
    label.after(ms = 5000, func = lambda: update_time(label))
    
    
