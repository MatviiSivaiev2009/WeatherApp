
import customtkinter as ctk 
import os
import modules.api_call as api
import modules.settings as set
from PIL import Image


PATH = os.path.abspath(__file__ + "/../../images")

widget = ctk.CTk(fg_color = "#5DA7B1")

widget.geometry(geometry_string = "350x350")

widget.title(string = "WeatherApp")

widget_border = ctk.CTkFrame(
    master = widget,
    border_width = 5,
    corner_radius = 0, 
    border_color = "#096C82",
    fg_color = "#5DA7B1",
    width = 351,
    height = 351
)
widget_border.place(x = 0, y = 0)

return_image = ctk.CTkImage(
    dark_image= Image.open(PATH + "/captcha.png"),
    size= (25, 25)
)

api.current_json = api.get_city_data(city= set.get_data('city'))

def enter_big_screen():
    import modules.big_screen as big_screen
    widget.withdraw() 
    big_screen.big_screen.mainloop()
    # window.destroy()

return_button = ctk.CTkButton(
    master= widget_border,
    text= "",
    fg_color= "#5DA7B1",
    hover_color= "#5DA7B1",
    image= return_image,
    corner_radius= 0,
    width= 25,
    height= 25,
    command= enter_big_screen
)
return_button.place(x = 300,y = 20)

weather_image = ctk.CTkImage(
    dark_image = Image.open(PATH + "/icon/" + set.find_image(weather= api.get_city_data(city= set.get_data('city')))),
    size = (150, 150)
)

weather_image_label = ctk.CTkLabel(
    master = widget_border,
    text = "",
    width = 140,
    height = 140,
    image = weather_image
)
weather_image_label.place(x = 20, y = 10)

city_position_label = ctk.CTkLabel(
    master = widget_border,
    text = set.get_data(name_data = "city"),
    text_color= "#FFFFFF",
    font = set.font(size_font = 40),
    width = 180
)
city_position_label.place(x = 160, y = 275)

temperature_label = ctk.CTkLabel(
    master= widget_border,
    text= f"{round(api.current_json['main']['temp'] - 273)}°",
    text_color= "#FFFFFF",
    font= set.font(size_font = 80),
    anchor= "e",
    width = 160
)
temperature_label.place(x = 180, y = 175)

description_label = ctk.CTkLabel(
    master= widget_border,
    text= f"{api.current_json['weather'][0]['description']}",
    text_color= "#FFFFFF",
    font = set.font(size_font = 16, bold= "bold"),
    anchor= "w",
    width = 140
)
description_label.place(x = 30, y = 185)

wheather_label = ctk.CTkLabel(
    master= widget_border,
    text= f"{api.current_json['weather'][0]['main']}",
    text_color= "#FFFFFF",
    font = set.font(size_font = 30, bold= "bold"),
    anchor= "w",
    width = 140,
)
wheather_label.place(x = 30, y = 152)

min_temp_label = ctk.CTkLabel(
    master = widget_border,
    text_color= "#FFFFFF",
    text = f"↓{round(api.current_json['main']['temp_min'] - 273)}°",
    font = set.font(size_font = 25)
)
min_temp_label.place(x = 30 ,y = 210)

max_temp_label = ctk.CTkLabel(
    master = widget_border,
    text_color= "#FFFFFF",
    text = f"↑{round(api.current_json['main']['temp_max'] - 273)}°",
    font = set.font(size_font = 25)
)
max_temp_label.place(x = 90, y = 210)

# widget.mainloop()



