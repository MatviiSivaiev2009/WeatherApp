#PARKING
import sqlite3 as sqlite, customtkinter as ctk
import modules.settings as set
import os

reg_window = ctk.CTk(fg_color= "#5DA7B1")

reg_window.title("WeatherApp - Regestration")

reg_window.geometry("460x645")

reg_window_border = ctk.CTkFrame(
    master= reg_window,
    border_width = 5,
    corner_radius = 0, 
    border_color = "#096C82",
    fg_color = "#5DA7B1",
    width = 461,
    height = 645
)
reg_window_border.place(x = 0, y = 0)

heading = ctk.CTkLabel(
    master = reg_window_border,
    text = "Реєстрація користува",
    height = 55,
    width = 380,
    font = set.font(size_font= 28),
    text_color= "#FFFFFF"
)
heading.place(x = 38, y = 42)

country_label = ctk.CTkLabel(
    master = reg_window_border,
    text = "Країна: ",
    height = 31,
    width = 87,
    font = set.font(size_font= 22),
    text_color= "#FFFFFF"
)
country_enter = ctk.CTkEntry(
    master = reg_window_border,
    height = 46,
    width = 218,
    border_width = 3,
    corner_radius = 20,
    border_color = "#DCE4EE",
    fg_color = "#096C82",
    font = set.font(size_font= 18),
)
country_enter.place(x = 38, y = 150)
country_label.place(x = 46, y = 108)

city_label = ctk.CTkLabel(
    master = reg_window_border,
    text = "Місто: ",
    height = 31, 
    width = 87,
    font = set.font(size_font= 22),
    text_color= "#FFFFFF"
)
city_enter = ctk.CTkEntry(
    master = reg_window_border,
    height = 46,
    width = 218,
    border_width = 3,
    corner_radius = 20,
    border_color = "#DCE4EE",
    fg_color = "#096C82",
    font = set.font(size_font= 18),
)
city_enter.place(x = 38, y = 249)
city_label.place(x = 46, y = 207)

name_label = ctk.CTkLabel(
    master = reg_window_border,
    text = "Ім'я: ",
    height = 31, 
    width = 87,
    font = set.font(size_font= 22),
    text_color= "#FFFFFF"
)
name_enter = ctk.CTkEntry(
    master = reg_window_border,
    height = 46,
    width = 295,
    border_width = 3,
    corner_radius = 20,
    border_color = "#DCE4EE",
    fg_color = "#096C82",
    font = set.font(size_font= 18),
)
name_enter.place(x = 38, y = 348)
name_label.place(x = 46, y = 306)

surname_label = ctk.CTkLabel(
    master = reg_window_border,
    text = "Прізвище: ",
    height = 31, 
    width = 87,
    font = set.font(size_font= 22),
    text_color= "#FFFFFF"
)
surname_enter = ctk.CTkEntry(
    master = reg_window_border,
    height = 46,
    width = 295,
    border_width = 3,
    corner_radius = 20,
    border_color = "#DCE4EE",
    fg_color = "#096C82",
    font = set.font(size_font= 18),
)
surname_enter.place(x = 38, y = 447)
surname_label.place(x = 46, y = 405)

def registration():
    path = os.path.abspath(__file__ + "/../../data_base")
    data_base = sqlite.connect(path + "/data_base.db")

    cursor = data_base.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user (name TEXT, surname TEXT, country TEXT, city TEXT, city_count INTEGER, current_pos TEXT)")
    data_base.commit()
     
    country = country_enter.get()
    city = city_enter.get()
    name = name_enter.get()
    surname = surname_enter.get()
    
    cursor.execute("INSERT INTO user (name, surname, country, city, city_count, Current_pos) VALUES (?,?,?,?,?,?)", (name, surname, country, city, 1, city))
    data_base.commit()
    data_base.close()
    reg_window.withdraw()
    import modules.cabinet as cabinet
    cabinet.window.mainloop()
    
    
        
button_save = ctk.CTkButton(
    master = reg_window_border, 
    width = 218,
    height = 46, 
    border_width = 3,
    corner_radius = 20,
    border_color = "#DCE4EE",
    fg_color = "#096C82",
    text = "Зберегти",
    font = set.font(size_font= 18),
    command = registration
)
button_save.place(x = 119, y = 546)

# reg_window.mainloop()