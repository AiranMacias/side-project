import requests
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QMainWindow, QLineEdit)
from PySide6.QtGui import (QIcon, QFont, QPixmap)
from PySide6.QtCore import Qt
import sys
from functools import partial

window_height = 300
window_width = 400
api_key = 'api key'


class WeatherApps(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Weather App')
        self.setFixedSize(window_width, window_height)
        centralWidget = QWidget(self)
        centralWidget.setStyleSheet("background-color:#505050")
        self.setCentralWidget(centralWidget)

        user_input_label = QLabel("Enter A City Name: ", self)
        user_input_label.setGeometry(0, -80, 200, 200)
        user_input_label.setFont(QFont("Sanserif", 15))
        user_input_label.setStyleSheet("color:green")

        self.user_input = QLineEdit(self)
        self.user_input.setGeometry(170, 10, 150, 25)
        self.user_input.setFont(QFont("Sanserif", 15))
        self.user_input.setPlaceholderText("Enter a city")

        self.search_button = QPushButton("Search", self)
        self.search_button.setGeometry(325, 10, 70, 25)
        self.search_button.clicked.connect(self.search_city)

        self.temp_label = QLabel(f"Temperature: ", self)
        self.temp_label.setGeometry(0, 50, 200, 25)
        self.temp_label.setFont(QFont("Sanserif", 15))

        self.weather_label = QLabel( self)
        self.weather_label.setGeometry(200, 100, 250, 25)
        self.weather_label.setFont(QFont("Sanserif", 15))

        self.city_name = QLabel(f"City: ", self)
        self.city_name.setGeometry(0, 80, 250, 25)
        self.city_name.setFont(QFont("Sanserif", 15))

        self.country = QLabel(f"Country: ", self)
        self.country.setGeometry(0, 110, 200, 25)
        self.country.setFont(QFont("Sanserif", 15))

        self.wind = QLabel(f"Wind Speed: ", self)
        self.wind.setGeometry(0, 140, 200, 25)
        self.wind.setFont(QFont("Sanserif", 15))
        self.weather_icon = QLabel(self)


# this function when the search button is clicked it gets the input from the Line edit and then searches for the city
# get then searches for the city get the data from the api and updates the labels and shows the temp,weather,weather icon  and city
    def search_city(self):
        search = self.user_input.text()
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={search}&units=metric&appid={api_key}")
        temp = weather_data.json()['main']['temp']
        weather = weather_data.json()['weather'][0]['description']
        city = weather_data.json()['name']
        country = weather_data.json()['sys']['country']
        wind = weather_data.json()['wind']['speed']
        icon = weather_data.json()['weather'][0]['icon']

        url = f'http://openweathermap.org/img/wn/{icon}@2x.png'
        response = requests.get(url)
        img = response.content
        pixmap = QPixmap()
        pixmap.loadFromData(img)
        self.weather_icon.setPixmap(pixmap)
        self.weather_icon.setGeometry(200, 50, 100, 50)

        self.temp_label.setText(f"Temperature: {temp}°C")
        self.weather_label.setText(f"{weather}")
        self.city_name.setText(f"City: {city}")
        self.country.setText(f'Country: {country}')
        self.wind.setText(f"Wind Speed: {wind}")
        
        
def main():
    weather_app = QApplication([])
    weather_app_window = WeatherApps()
    weather_app_window.show()
    sys.exit(weather_app.exec())


if __name__ == "__main__":
    main()
