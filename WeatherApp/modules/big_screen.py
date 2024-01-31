# PARKING 

# 
import customtkinter as ctk
import modules.api_call as call
import modules.city_info as cinfo
import modules.forecast_info as finfo
import modules.settings as set
import os
from PIL import Image
import time
import asyncio

#
PATH = os.path.abspath(__file__ + "/../../images")

big_screen = ctk.CTkToplevel(fg_color = "#5DA7B1")

big_screen.geometry(geometry_string = "1200x750")

big_screen.title(string = "WeatherApp")

big_screen_frame = ctk.CTkFrame(
    master= big_screen,
    width= 1200,
    height= 751,
    fg_color= "#5DA7B1",
    border_color= "#096C82",
    border_width= 5,
    corner_radius= 0
)
big_screen_frame.place(x = 0, y = 0)

image_profile = ctk.CTkImage(light_image = Image.open(PATH + "/user.png"), size = (50,50))

def enter_cabinet():
    import modules.cabinet as cabinet
    big_screen.withdraw()
    try:
        cabinet.window.deiconify()
    except:
        pass
    cabinet.window.mainloop()

image_profile_button = ctk.CTkButton(
    master = big_screen,
    image = image_profile,
    text = "",
    fg_color = "#5DA7B1",
    hover_color =  "#5DA7B1",
    width = 0,
    height = 0,
    command = enter_cabinet
)
image_profile_button.place(x = 318, y = 25)

name_label = ctk.CTkLabel(
    master= big_screen, 
    text= f"{set.get_data(name_data= 'name')} {set.get_data(name_data='surname')}",
    text_color= "#FFFFFF",
    font= set.font(size_font = 14)
)
name_label.place(x = 380, y = 38)

entry_bg = ctk.CTkFrame(
    master = big_screen,
    height = 46, 
    width = 218,
    border_width = 3,
    corner_radius = 20,
    border_color = "#a8cee0",
    fg_color = "#096C82",
)
entry_bg.place(x = 918, y = 31)

city_entry = ctk.CTkEntry(
    master = big_screen,
    height = 36, 
    width = 180,
    placeholder_text = "Пошук",
    corner_radius = 20,
    border_color = "#096C82",
    fg_color = "#096C82",
    bg_color = "#096C82",
    font = set.font(size_font = 18),
    placeholder_text_color = "#a8cee0"
)
city_entry.place(x = 943, y = 35)

city_frame = ctk.CTkScrollableFrame(
    master = big_screen,
    height = 800,
    width = 275,
    fg_color = "#096C82",
    corner_radius = 0,
    scrollbar_button_color = "#096C82",
    scrollbar_button_hover_color = "#096C82",
)
city_frame.place(x = 0, y = 0)

current_position = cinfo.Current_Position(city_name = set.get_data(name_data = "city"), master = city_frame)
current_position.place_self()
# 
def add_city():
    info_label = cinfo.City_info(city_name= city_entry.get(), master = city_frame)
    info_label.place_self()
    city_entry.delete(0, "end")
# 
search_image = ctk.CTkImage(
    dark_image = Image.open(PATH + "/magnifying.png"),
    size = (25,25)
)
    
search_button = ctk.CTkButton(
    master = big_screen,
    text = "", 
    image = search_image,
    width = 20,
    height = 20,
    corner_radius = 0,
    fg_color = "#096C82",
    bg_color = "#096C82",
    hover_color =  "#096C82",
    command = add_city
)
search_button.place(x = 928, y = 37)   

position_label = ctk.CTkLabel(
    master = big_screen,
    text = "Поточна позиція",
    text_color= "#FFFFFF",
    font = set.font(size_font = 35),
    width = 314
)
position_label.place(x = 576, y = 101)

city_position_label = ctk.CTkLabel(
    master = big_screen,
    text = set.get_data(name_data = "current_pos"),
    text_color= "#FFFFFF",
    font = set.font(size_font = 22),
    width = 87
)
city_position_label.place(x = 689, y = 162)

temperature_label = ctk.CTkLabel(
    master= big_screen,
    text= f"{round(call.current_json['main']['temp'] - 273)}°",
    text_color= "#FFFFFF",
    font= set.font(size_font = 80),
    width = 87
)
temperature_label.place(x = 690, y = 190)

wheather_label = ctk.CTkLabel(
    master= big_screen,
    text= f"{call.current_json['weather'][0]['main']}",
    text_color= "#FFFFFF",
    font = set.font(size_font = 30),
    width = 140,
)
wheather_label.place(x = 663, y = 284)

description_label = ctk.CTkLabel(
    master= big_screen,
    text= f"{call.current_json['weather'][0]['description']}",
    text_color= "#FFFFFF",
    font = set.font(size_font = 16),
    width = 140
)
description_label.place(x = 663, y = 318)

min_temp_label = ctk.CTkLabel(
    master = big_screen,
    text_color= "#FFFFFF",
    text = f"↓{round(call.current_json['main']['temp_min'] - 273)}°",
    font = set.font(size_font = 30)
)
min_temp_label.place(x = 743,y = 345)

max_temp_label = ctk.CTkLabel(
    master = big_screen,
    text_color= "#FFFFFF",
    text = f"↑{round(call.current_json['main']['temp_max'] - 273)}°",
    font = set.font(size_font = 30)
)
max_temp_label.place(x = 678, y = 345)

weather_image = ctk.CTkImage(
    dark_image = Image.open(PATH + "/icon/" + set.find_image(weather = call.get_city_data(city = set.get_data('current_pos')))),
    size = (170, 170)
)

weather_image_label = ctk.CTkLabel(
    master = big_screen,
    text = "",
    width = 170,
    height = 170,
    image = weather_image
)
weather_image_label.place(x = 380, y = 170)

weekdate_label = ctk.CTkLabel(
    master= big_screen,
    text_color= "#FFFFFF",
    text= f"{set.list_date[0]}",
    font = set.font(size_font=22),
    width = 115  
)
weekdate_label.place(x = 956, y = 191)

date_label = ctk.CTkLabel(
    master = big_screen,
    text_color= "#FFFFFF",
    text = f"{set.list_date[1]}",
    font = set.font(size_font = 40)
)
date_label.place(x = 936, y = 227)

time_label = ctk.CTkLabel(
    master = big_screen,
    text_color= "#FFFFFF",
    text = f"{set.list_date[2]}",
    font = set.font(size_font = 30)
)

time_label.place(x = 974, y = 274)
time_label.after(ms = 5000, func = lambda: set.update_time(time_label))


forecast_frame = ctk.CTkScrollableFrame(
    master = big_screen,
    orientation = "horizontal",
    width = 748 ,
    height = 200,
    corner_radius = 20,
    border_width = 5,
    fg_color = "#5DA7B1",
    border_color = "#EEEEFF",
    scrollbar_fg_color = "#5DA7B1",
    scrollbar_button_color= "#5DA7B1",
    scrollbar_button_hover_color= "#5DA7B1"
)
forecast_frame.place(x=345, y=430)

white_line_image = ctk.CTkImage(
    dark_image= Image.open(PATH + "/white_line.png"),
    size= (753, 5)
)

white_line = ctk.CTkLabel(
    master= big_screen,
    text= "",
    image= white_line_image
)
white_line.place(x = 360, y= 654)

forecast_info = finfo.ForecastInfo(master= forecast_frame)
forecast_info.create_forecast()

current_pos_check = None
def update_position():
    global current_pos_check, current_position   
    if current_pos_check == set.get_data("current_pos"):
        call.current_json = call.get_city_data(set.get_data("current_pos"))
        city_position_label.configure(text = f"{set.get_data('current_pos')}")
        temperature_label.configure(text= f"{round(call.current_json['main']['temp'] - 273)}°")
        wheather_label.configure(text= f"{call.current_json['weather'][0]['main']}")
        description_label.configure(text= f"{call.current_json['weather'][0]['description']}")
        min_temp_label.configure(text = f"↓{round(call.current_json['main']['temp_min'] - 273)}°")
        max_temp_label.configure(text = f"↑{round(call.current_json['main']['temp_max'] - 273)}°")
        weather_image.configure(dark_image = Image.open(PATH + "/icon/" + set.find_image(weather = call.get_city_data(city = set.get_data('current_pos')))))
        weather_image_label.configure(image = weather_image)
        # current_position.delete_self()
        current_position = cinfo.Current_Position(city_name = f"{set.get_data('current_pos')}", master = city_frame)
        current_position.place_self()
        

    current_pos_check = set.get_data("current_pos")
    city_position_label.after(ms = 1000, func = update_position)

city_position_label.after(ms = 1000, func = update_position)