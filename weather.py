import requests
from config import API_KEY

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code != 200:
        print("❌ City not found!")
        return
    
    data = response.json()

    print("\n----- Weather Report -----")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Pressure:", data["main"]["pressure"], "hPa")
    print("Weather:", data["weather"][0]["description"])
    print("--------------------------\n")


def main():
    while True:
        city = input("Enter city name: ")
        get_weather(city)

        again = input("Search another city? (y/n): ")
        if again.lower() != "y":
            break

if __name__ == "__main__":
    main()
