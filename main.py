from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
import requests
from bs4 import BeautifulSoup

class Weather(MDApp):
    def get_weather(self, city):
        url = f"https://www.google.com/search?q=weather+in+{city.replace(' ','+')}+now"
        response = requests.get(url)
        
        if response.status_code == 200:
            self.img.source = "weather.png"
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Fetching weather information
            try:
                temp = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text.replace('درجة مئوية','°')
                return f"Temperature: {temp}"
            except Exception as e:
                self.img.source = "404.png"
                return "Oops! City not found :("

    def build(self):
        self.theme_cls.primary_palette = "Blue"

        screen = Screen()

        self.city_input = MDTextField(
            hint_text="Enter city name",
            pos_hint={'center_x': 0.5, 'center_y': 0.8},
            size_hint_x=None,
            width=600
        )
        screen.add_widget(self.city_input)
        
        self.img = Image(
            source="weather.png",
            pos_hint={"center_y":0.55,"center_x":0.5},
        )
        screen.add_widget(self.img)
        
        self.weather_label = MDLabel(
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            size_hint_y=None,
            height=50,
            font_style="H5",
        )
        screen.add_widget(self.weather_label)

        self.fetch_button = MDIconButton(
            icon="magnify",
            pos_hint={'center_x': 0.8, 'center_y': 0.798},
            on_release=self.show_weather
        )
        screen.add_widget(self.fetch_button)
        self.now_button = MDIconButton(
            icon="map-marker-radius",
            pos_hint={'center_x': 0.9, 'center_y': 0.798},
            on_release=self.current_weather
        )
        screen.add_widget(self.now_button)
        
        return screen

    def show_weather(self, *args):
        city = self.city_input.text
        if not city:
            city = "Alexandria"
        weather_info = self.get_weather(city)
        self.weather_label.text = weather_info

    def current_weather(self, *args):
        self.city_input.text = ""
        city = "Alexandria"
        weather_info = self.get_weather(city)
        self.weather_label.text = weather_info

if __name__ == '__main__':
    Weather().run()