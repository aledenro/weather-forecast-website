import streamlit as st
import plotly.express as px
from backend import get_data

IMAGES = {"Clear": "images/clear.png",
          "Clouds": "images/cloud.png",
          "Rain": "images/rain.png",
          "Snow": "images/snow.png"}

st.title("Weather Forecast for the Next Days")

location = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days.")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {location}:")

if location:
    data = get_data(location, days)
    if data is not None:
        if option == "Temperature":
            temperatures = [dict_data["main"]["temp"] / 10 for dict_data in data]
            dates = [dict_data["dt_txt"] for dict_data in data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        elif option == "Sky":
            filtered_data = [dict_data["weather"][0]["main"] for dict_data in data]
            image_paths = [IMAGES[condition] for condition in filtered_data]
            st.image(image_paths, width=115)
    else:
        st.warning("Please type a valid location!")