import requests

# Please get an api key from https://openweathermap.org/ and use it here
API_KEY = ""


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 404:
        return None
    else:
        data = response.json()
        filtered_data = data["list"]
        num_values = forecast_days * 8
        filtered_data = filtered_data[:num_values]

        return filtered_data


if __name__ == "__main__":
    print(get_data("Tokyo", 3, "Temperature"))