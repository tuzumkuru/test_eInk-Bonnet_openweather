# eInk Bonnet with OpenWeather

A test application to control eInk Bonnet with Python

Uses OpenWeather API to get weather data and prints the data on a Adafruit eInk Bonnet Display: https://www.adafruit.com/product/4687

Started the project with the example code provided by Adafruit: https://learn.adafruit.com/raspberry-pi-e-ink-weather-station-using-python

## Usage 

Pipenv is being used to manage Python packages

After cloning the project just use

    pipenv install
  
to install the required packages. 

python-dotenv is used to manage the environment variables. Rename .env_example file to .env and type your API Key in the corresponding place. 

You can get your API Key after signing up and logging into OpenWeatherMap. You can find your API keys at https://home.openweathermap.org/api_keys address.

You can run the application using pipenv 

    pipenv run python main.py

## Troubleshooting

There are some potential problems and solutions that you can encounter below. For other problems, feel free to get in touch

### libopenjp2-7
If you encounter an error about libopenjp2-7 you can install it using the command below:

    sudo apt-get install libopenjp2-7

### OSError: /dev/spidev0.0 does not exist

This error probably means that you did not enable the SPI Interface. For Raspberry Pi open raspi-config

    sudo raspi-config

Go to 3. Interface Options -> I4 SPI -> Choose Yes for enabling the SPI interface. 
