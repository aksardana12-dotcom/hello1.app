import streamlit as st
import requests
from gtts import gTTS
from io import BytesIO
st.set_page_config(
    page_title= "AI weather bot"
    page_icon = "(╯°□°）╯︵ ┻━┻"
)

st.title("AI weather")
st.write("Enter any city and get live weather")

def get_city(city)
    url = f"geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

    data = requests.get(url).json()

    if "results" in data:
        return data["results"][0]
    
    return None


def get_weather(lat, lon):

    url = (
        f"https://api.open-meteo.com/v1forecast?"
        f"latitude={lat}$longitude={lon}"
        "&current=temperature_2m,wind_speed_10m"
        "&dailyprecipitation_probablility_max"
    )

    return requests.get(rul).json()

def advice(temp,rain):
    if temp > 30:
        return f"it is currently {temp} degrees, which is pretty hot"
    elif temp < 10: 
        return f"it is currently {temp} degrees, which is pretty cold"
    elif rain > 50:
        return f"chance of precipitation is {rain} today. maybe get an umbrella or something"
    else:

        
        return f"weather looks good"
    
    def speak (text)
        
        audio = BytesIOO()

        tts = gTTS(text)

        tts.write_to_fp(audio)

        return audio
    


    city - st.text_input(
        "what city would you like to view?",
        "Hell, Norway"
    )

    if st.button("Check Weather"):

        place = get_city(city)

        if place:

            lat = place["latitude"]
            lon = place["longitude"]

            weather = get_weather(
                lat,
                lon
            )
            

            temp_c = weather["current"]["temperature_2m"]

            temp_f = round(
                temp_c * 9/5 + 32,
                1
            )
            
            wind = weather["current"]["wind_speed_10m"]

            rain = weather["daily"]["precipitation_probablility_max"][0]

            msg = advice(
                temp_c,
                rain
            )

            st.success(
                f"""
         🏙️ {city}

         temperature:
         {temp_c}°C | {temp_f}°F

         Wind:
         {wind} km/h

        Rain:
        {rain}%

        AI Advice:
        {msg}
        """
            )


            speech = f"""
            The temperature in {city} is {temp_c} degrees celcius, and {temp_f} degrees fahrenheit.

            Rain probability is {rain}%.
            {msg}
"""
            
            audio = speak(speech)

            st.audio(
                audio,
                format= "audio/mp3"
            )
            
        else:
            st.error("city not found :(")