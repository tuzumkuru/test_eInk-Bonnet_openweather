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

If you encounter an error about libopenjp2-7 you can install it using the command below:

    sudo apt-get install libopenjp2-7

For other errors, feel free to get in touch
