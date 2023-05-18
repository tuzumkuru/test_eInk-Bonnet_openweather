# SPDX-FileCopyrightText: 2020 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

from datetime import datetime
import json
from PIL import Image, ImageDraw, ImageFont
from adafruit_epd.epd import Adafruit_EPD

small_font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16
)
medium_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
large_font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24
)
icon_font = ImageFont.truetype("./meteocons.ttf", 48)

# Map the OpenWeatherMap icon code to the appropriate font character
# See http://www.alessioatzeni.com/meteocons/ for icons
ICON_MAP = {
    "01d": "B",
    "01n": "C",
    "02d": "H",
    "02n": "I",
    "03d": "N",
    "03n": "N",
    "04d": "Y",
    "04n": "Y",
    "09d": "Q",
    "09n": "Q",
    "10d": "R",
    "10n": "R",
    "11d": "Z",
    "11n": "Z",
    "13d": "W",
    "13n": "W",
    "50d": "J",
    "50n": "K",
}

# RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Weather_Graphics:
    def __init__(self, display, *, am_pm=True, unit="C"):
        self.am_pm = am_pm
        self.unit = unit

        self.small_font = small_font
        self.medium_font = medium_font
        self.large_font = large_font

        self.display = display

        self._weather_icon = None
        self._city_name = None
        self._main_text = None
        self._temperature_text = None
        self._description = None
        self._time_text = None

    def display_weather(self, weather):
        weather = json.loads(weather.decode("utf-8"))

        # set the icon/background
        self._weather_icon = ICON_MAP[weather["weather"][0]["icon"]]

        city_name = weather["name"] + ", " + weather["sys"]["country"]
        print(city_name)
        self._city_name = city_name

        main = weather["weather"][0]["main"]
        print(main)
        self._main_text = main

        temperature = weather["main"]["temp"] - 273.15  # its...in kelvin
        print(temperature)
        if self.unit == "C":
            self._temperature_text = "%d °C" % temperature
        elif self.unit == "F":
            self._temperature_text = "%d °F" % ((temperature * 9 / 5) + 32)
        else: 
            self._temperature_text = "%d °C | %d °F" % (temperature, (temperature * 9 / 5) + 32)

        description = weather["weather"][0]["description"]
        description = description[0].upper() + description[1:]
        print(description)
        self._description = description
        # "thunderstorm with heavy drizzle"

        self.update_time()

    def update_time(self):
        now = datetime.now()
        old_time_text = self._time_text
        self._time_text = now.strftime("%I:%M %p").lstrip("0").replace(" 0", " ")
        if(old_time_text != self._time_text):
            self.update_display()

    def update_display(self):
        self.display.fill(Adafruit_EPD.WHITE)
        image = Image.new("RGB", (self.display.width, self.display.height), color=WHITE)
        draw = ImageDraw.Draw(image)

        # Draw the city
        draw.text(
            (5, 5), self._city_name, font=self.medium_font, fill=BLACK,
        )

        # Draw the time
        (font_width, font_height) = large_font.getsize(self._time_text)
        draw.text(
            (5, font_height * 2),
            self._time_text,
            font=self.large_font,
            fill=BLACK,
        )

        # Draw the Icon
        (font_width, font_height) = icon_font.getsize(self._weather_icon)
        draw.text(
            (
                self.display.width - font_width - 5,
                0,
            ),
            self._weather_icon,
            font=icon_font,
            fill=BLACK,
        )       

        previous_font_height = font_height
        # Draw the main text
        (font_width, font_height) = large_font.getsize(self._main_text)
        draw.text(
            (self.display.width - font_width - 5, previous_font_height),
            self._main_text,
            font=self.large_font,
            fill=BLACK,
        )

        previous_font_height = previous_font_height + font_height
        # Draw the description
        (font_width, font_height) = small_font.getsize(self._description)
        draw.text(
            (self.display.width - font_width - 5, previous_font_height),
            self._description,
            font=self.small_font,
            fill=BLACK,
        )

        # Draw the temperature
        (font_width, font_height) = large_font.getsize_multiline(self._temperature_text)
        draw.text(
            (
                self.display.width - font_width - 5,
                self.display.height - font_height - 5,
            ),
            self._temperature_text,
            font=self.large_font,
            fill=BLACK,
        )

        self.display.image(image)
        self.display.display()
