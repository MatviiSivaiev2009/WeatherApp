#PARKING
import customtkinter
import sqlite3
import os
import modules.settings as set
from PIL import Image

PATH = os.path.abspath(__file__ + "/../../images")

window = customtkinter.CTkToplevel(fg_color = "#5DA7B1")

window.title("WeatherApp - Personal Cabinet")

window.geometry("460x645")

window_border = customtkinter.CTkFrame(
    master= window,
    border_width = 5,
    corner_radius = 0, 
    border_color = "#096C82",
    fg_color = "#5DA7B1",
    width = 461,
    height = 645
)
window_border.place(x = 0, y = 0)

heading = customtkinter.CTkLabel(
    master = window,
    text = "Особистий кабінет",
    height = 55,
    width = 380,
    text_color = "#FFFFFF",
    font = set.font(size_font = 28)
)
heading.place(x = 38, y = 42)

country_label = customtkinter.CTkLabel(
    master = window,
    text = "Країна: ",
    height = 31,
    width = 87,
    text_color = "#FFFFFF",
    font = set.font(size_font = 22)
)

country_data = customtkinter.CTkLabel(
    master = window,
    text = set.get_data("country"),
    height = 31,
    width = 196,
    text_color = "#FFFFFF",
    font = set.font(size_font = 28, underline = True)
)
country_data.place(x = 119, y = 157)
country_label.place(x = 46, y = 108)

city_label = customtkinter.CTkLabel(
    master = window,
    text = "Місто: ",
    height = 31,
    width = 87,
    text_color = "#FFFFFF",
    font = set.font(size_font = 22)
)

city_data = customtkinter.CTkLabel(
    master = window,
    text = set.get_data("city"),
    height = 31,
    width = 196,
    text_color = "#FFFFFF",
    font = set.font(size_font = 28, underline = True)
     
)
city_data.place(x = 119, y = 256)
city_label.place(x = 46, y = 207)


name_label = customtkinter.CTkLabel(
    master = window,
    text = "Ім'я: ",
    height = 31,
    width = 87,
    text_color = "#FFFFFF",
    font = set.font(size_font = 22)
)

name_data = customtkinter.CTkLabel(
    master = window,
    text = set.get_data("name"),
    height = 31,
    width = 196,
    text_color = "#FFFFFF",
    font = set.font(size_font = 28, underline = True)
)
name_data.place(x = 119, y = 352)
name_label.place(x = 46, y = 306)

surname_label = customtkinter.CTkLabel(
    master = window,
    text = "Прізвіще: ",
    height = 31,
    width = 87,
    text_color = "#FFFFFF",
    font = set.font(size_font = 22)
)

surname_data = customtkinter.CTkLabel(
    master = window,
    text = set.get_data("surname"),
    height = 31,
    width = 196,
    text_color = "#FFFFFF",
    font = set.font(size_font = 28, underline = True)
)

surname_data.place(x = 119, y = 455)
surname_label.place(x = 46, y = 405)

def enter_big_screen():
    import modules.big_screen as big_screen 
    big_screen.big_screen.deiconify()
    window.withdraw()
    

app_button = customtkinter.CTkButton(
    master = window,
    width = 218,
    height = 46,
    border_width = 3,
    corner_radius = 20,
    border_color = "#FFFFFF",
    fg_color = "#096C82",
    text = "Перейти до додатку",
    text_color = "#FFFFFF",
    font = set.font(size_font = 18),
    command = enter_big_screen
)

exit_label = customtkinter.CTkLabel(
    master= window,
    text = "Вихід",
    text_color = "#FFFFFF",
    font = set.font(size_font = 14)   
)

exit_label.place(x= 368, y = 20)
app_button.place(x = 119, y = 546)

exit_image = customtkinter.CTkImage(
   dark_image = Image.open(PATH + "/left_arrow.png"),
   size = (29, 29) 
)

def exit_account():
    set.database_command(string = "DELETE FROM user" )
    try:
        import modules.big_screen as big_screen
        big_screen.big_screen.destroy()
    except:
        pass
    try:
        import modules.widget as widget
        widget.widget.destroy()
    except:
        pass
    try:
        import modules.reg as reg
        reg.reg_window.destroy()
    except:
        pass
    try:
        window.destroy()
    except:
        pass

exit_button = customtkinter.CTkButton(
    master = window,
    text = "",
    image = exit_image,
    fg_color = "#5DA7B1",
    hover_color = "#5DA7B1",
    height = 0,
    width = 0,
    command = exit_account
)
exit_button.place(x = 410, y = 17)
