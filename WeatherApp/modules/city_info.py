#PARKING
import customtkinter as ctk
import modules.api_call as api_call
import modules.settings as set
import tkinter


class City_info():
    def __init__(self, city_name, master):
        self.city_name = city_name
        self.master = master
        self.city_info()
        self.create_label()   
        self.row = set.get_data('city_count')
        set.database_command(f"UPDATE user SET city_count = {set.get_data('city_count') + 1}")
        
    def city_info(self):
        self.city_data = api_call.get_city_data(self.city_name)

    
    
    def create_label(self):
        self.frame = ctk.CTkFrame(
            master = self.master,
            width = 276,
            height = 101,
            corner_radius = 20,
            border_width = 2,
            fg_color = "#096C82",
            border_color = "#FFFFFF"
        )
        
        def set_as_current():
            set.database_command(f"UPDATE user SET current_pos = (\"{self.city_name}\") WHERE city LIKE \"{set.get_data('city')}\"")       
        
        self.place_label = ctk.CTkButton(
            master = self.frame,
            width = 153,
            height = 10,
            text = f"{self.city_name}",
            text_color = "#FFFFFF",
            font = set.font(size_font= 16, bold = "bold"),
            anchor = "w",
            command = set_as_current,
            fg_color = "#096C82"
            #fg_color = "#060606"
        )
        self.time_label = ctk.CTkLabel(
            master = self.frame,
            width = 153,
            text = set.list_date[2],
            text_color = "#FFFFFF",
            font = set.font(12),
            anchor = "nw",
            #fg_color = "#060606"
        )
        self.time_label.after(ms = 5000, func = lambda: set.update_time(self.time_label))
        self.temp_label = ctk.CTkLabel(
            master = self.frame,
            width = 80,
            text = f"{round(self.city_data['main']['temp'] -273)}°",
            text_color = "#FFFFFF",
            font = set.font(50),
            anchor = "e",
            #fg_color = "#060606"
        )
        self.weather_status = ctk.CTkLabel(
            master = self.frame,
            width = 104,
            text = f"{self.city_data['weather'][0]['main']}",
            text_color = "#FFFFFF",
            font = set.font(12),
            anchor = "w"
        )
        self.temp_varr = ctk.CTkLabel(
            master = self.frame,
            width = 107,
            text = f"макс.:{round(self.city_data['main']['temp_max'] - 273)}°, мін.:{round(self.city_data['main']['temp_min'] - 273)}°",
            text_color = "#FFFFFF",
            font = set.font(size_font = 12),
            anchor = "e"
        )
        
        


        # self.button = ctk.CTkButton(
        #     master = self.frame,
        #     width = 276,
        #     height = 101,
        #     corner_radius = 20,
        #     border_width = 2,
        #     fg_color = "#096C82",
        #     border_color = "#FFFFFF",
        #     text = "",
        #     command = set_as_current
        # )

        self.place_label.grid(column = 0, row = 0, columnspan = 2, sticky = tkinter.E, padx = (8, 0), pady = (10, 0))
        self.time_label.grid(column = 0, row = 1 , columnspan = 2, sticky = tkinter.E, padx = (3, 0))
        self.temp_label.grid(column = 2, row = 0, rowspan = 2, sticky = tkinter.E, pady = (10, 0))
        self.weather_status.grid(column = 0, row = 2, columnspan = 2)
        self.temp_varr.grid(column = 1, row = 2, columnspan = 2)
        
    def place_self(self):
        
        self.frame.grid(column = 0, row = self.row, padx = 20, pady = 20, ipadx = 5, ipady = 5)
         
           
class Current_Position():
    def __init__(self, city_name, master):
        self.city_name = city_name
        self.master = master
        self.city_info()
        self.create_label()   
        self.row = 0
        set.database_command(f"UPDATE user SET city_count = {set.get_data('city_count') + 1}")
        
    def city_info(self):
        self.city_data = api_call.get_city_data(self.city_name)
    
    def create_label(self):
        self.frame = ctk.CTkFrame(
            master = self.master,
            width = 276,
            height = 101,
            corner_radius = 20,
            border_width = 2,
            bg_color = "#096C82",
            fg_color = "#4599A4",
            border_color = "#FFFFFF"
        )       
        self.place_label = ctk.CTkLabel(
            master = self.frame,
            width = 153,
            height = 10,
            text = f"Поточна позиція",
            text_color = "#FFFFFF",
            font = set.font(size_font= 16, bold = "bold"),
            anchor = "w",
            #fg_color = "#060606"
        )
        self.city_label = ctk.CTkLabel(
            master = self.frame,
            width = 153,
            text = f"{self.city_name}",
            text_color = "#FFFFFF",
            font = set.font(12),
            anchor = "nw",
            #fg_color = "#060606"
        )
        self.temp_label = ctk.CTkLabel(
            master = self.frame,
            width = 80,
            text = f"{round(self.city_data['main']['temp'] -273)}°",
            text_color = "#FFFFFF",
            font = set.font(50),
            anchor = "e",
            #fg_color = "#060606"
        )
        self.weather_status = ctk.CTkLabel(
            master = self.frame,
            width = 104,
            text = f"{self.city_data['weather'][0]['main']}",
            text_color = "#FFFFFF",
            font = set.font(12),
            anchor = "w"
        )
        self.temp_varr = ctk.CTkLabel(
            master = self.frame,
            width = 107,
            text = f"макс.:{round(self.city_data['main']['temp_max'] - 273)}°, мін.:{round(self.city_data['main']['temp_min'] - 273)}°",
            text_color = "#FFFFFF",
            font = set.font(size_font = 12),
            anchor = "e"
        )
        self.place_label.grid(column = 0, row = 0, columnspan = 2, sticky = tkinter.E, padx = (8, 0), pady = (10, 0))
        self.city_label.grid(column = 0, row = 1 , columnspan = 2, sticky = tkinter.E)
        self.temp_label.grid(column = 2, row = 0, rowspan = 2, sticky = tkinter.E, pady = (10, 0))
        self.weather_status.grid(column = 0, row = 2, columnspan = 2)
        self.temp_varr.grid(column = 1, row = 2, columnspan = 2)

    def place_self(self):
        self.frame.grid(column = 0, row = self.row, padx = 20, pady = 20, ipadx = 5, ipady = 5)

    def delete_self(self):
        self.frame.destroy()