import requests

url = "http://api.open-notify.org/iss-now.json"

MY_LAT = "42.984268"
MY_LONG = "-81.247528"
parameters = {

}

response = requests.get(url)
data = response.json()
print(data)

sat_lattitude = data["iss_position"]["latitude"]
sat_longiitude = data["iss_position"]["longitude"]

print(f"Lat is {sat_lattitude}")
print(f"lons is {sat_longiitude}")


def check_SAT_near_location():
    if MY_LAT - 5 <= sat_lattitude <= MY_LAT + 5 and MY_LONG -5 <= sat_longiitude <= MY_LONG + 5:
        print("Sat is over current location")
        return True











