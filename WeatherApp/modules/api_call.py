#PARKING
import requests
import modules.settings as set

api_key = "39e675083693cd27d6683d43653c3015"

url_forecast = f"https://api.openweathermap.org/data/2.5/forecast?q={set.get_data(name_data='current_pos')},{set.get_data(name_data='country')}&appid={api_key}"

url_current = f"https://api.openweathermap.org/data/2.5/weather?q={set.get_data(name_data='current_pos')},{set.get_data(name_data='country')}&appid={api_key}"

response_current = requests.get(url= url_current)

if response_current.status_code == 200:
    current_json = response_current.json()
# else:
#     print(response_current.status_code)

def get_city_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url = url)
    if response_current.status_code == 200:
        return response.json() 
      
def get_forecast_data():
    response = requests.get(url = url_forecast)
    if response_current.status_code == 200:
        return response.json()