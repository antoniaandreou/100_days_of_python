import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758


def is_iss_overhead():
    """
    Checks if the ISS is +-5 degrees from our latitude and longitude defined in the global variables MY_LAT & MY_LONG
    :return: Boolean
    """
    # Call the ISS API to get its coordinates
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # Get ISS position
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]
    coordinates = (round(float(latitude)), round(float(longitude)))
    print(coordinates)

    # Check if ISS is nearby and visible
    if round(coordinates[0]) in range(int(MY_LAT) - 5, int(MY_LAT) + 5) and round(coordinates[1]) in range(
            int(MY_LONG) - 5, int(MY_LONG) + 5):
        return True


def is_dark():
    """
    Check if it is dark outside.
    :return: Boolean
    """
    # Get information on sunset and sunrise
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response_ss = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response_ss.raise_for_status()
    data_ss = response_ss.json()
    sunrise = int(data_ss["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_ss["results"]["sunset"].split("T")[1].split(":")[0])

    # Get current time
    current_time = datetime.now()
    current_hour = current_time.hour
    print(current_hour)

    if current_hour < sunrise or current_hour > sunset:
        return True


# Main

if is_iss_overhead() and is_dark():
    print("LOOK UP!")
elif is_iss_overhead() and not is_dark():
    print("Pity is daytime and you can't see it!")
else:
    print(f"The ISS is not near by!")
