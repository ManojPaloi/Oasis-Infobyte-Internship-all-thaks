import tkinter as tk
from tkinter import ttk
import requests

# Function to fetch weather data from API
def get_weather():
    city = city_entry.get()
    api_key = '0520afd080e41d4a23fd49453e192768'  # Replace with your API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        weather_data = response.json()

        # Check if 'name' key exists in weather_data
        if 'name' in weather_data:
            location_label.config(text=f"Weather in {weather_data['name']}, {weather_data['sys']['country']}")
            temp_label.config(text=f"{weather_data['main']['temp']}°C")
            weather_label.config(text=weather_data['weather'][0]['description'])
        else:
            location_label.config(text="City not found")
            temp_label.config(text="")
            weather_label.config(text="")
    
    except requests.exceptions.RequestException as e:
        location_label.config(text="Error fetching data")
        temp_label.config(text="")
        weather_label.config(text="")

# Create main window
root = tk.Tk()
root.title('Weather App')

# Create widgets
city_label = ttk.Label(root, text='City:')
city_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = ttk.Entry(root, width=30)
city_entry.grid(row=0, column=1, padx=10, pady=10)

get_weather_button = ttk.Button(root, text='Get Weather', command=get_weather)
get_weather_button.grid(row=0, column=2, padx=10, pady=10)

location_label = ttk.Label(root, text='', font=('Helvetica', 20, 'bold'))
location_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

temp_label = ttk.Label(root, text='', font=('Helvetica', 40))
temp_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

weather_label = ttk.Label(root, text='')
weather_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Start the main loop
root.mainloop()
