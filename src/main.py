import sys
import requests

def get_forecast(key, latitude, longitude,):

    url = "https://data.hub.api.metoffice.gov.uk/sitespecific/v0/point/daily"

    headers = {'accept': "application/json",
               'apikey': key}
    params = {
        'excludeParameterMetadata' : "FALSE",
        'includeLocationName' : "TRUE",
        'latitude' : latitude,
        'longitude' : longitude
        }

    result = requests.get(url, headers=headers, params=params)

    return result.json()


def get_next_3_days_data(weather_list):
    if type(weather_list) == list:
        return(weather_list[1:4])
    else:
        raise ValueError


def get_rain_probabilities(daily_weather):
    daily_rain_dict = {
    "time": daily_weather["time"],
    "probability_of_rain": max(daily_weather["dayProbabilityOfRain"], daily_weather["nightProbabilityOfRain"])
    }
    return(daily_rain_dict)


def determine_highest_probability(three_day_weather):
    return max(three_day_weather, key=lambda x: x['probability_of_rain'])


def determine_rain_likelihood(daily_weather_dict):
    prob_rain = daily_weather_dict["probability_of_rain"]
    if prob_rain >= 80:
        return(f"It is very likely to rain on {daily_weather_dict['time'].replace('T00:00Z', '')}")
    elif 50 <= prob_rain < 80:
        return(f"It is likely to rain on {daily_weather_dict['time'].replace('T00:00Z', '')}")
    else:
        return(f"WATER YOUR PLANTS!")


def main():

    key = sys.argv[1]
    latitude = sys.argv[2]
    longitude = sys.argv[3]

    forecast = get_forecast(key, latitude, longitude)
    data  = forecast["features"][0]["properties"]["timeSeries"]
    three_day_weather = get_next_3_days_data(data)

    probability_rain_list = []
    for i in range(len(three_day_weather)):
        x = get_rain_probabilities(three_day_weather[i])
        probability_rain_list.append(x)

    highest_prob = determine_highest_probability(probability_rain_list)

    return("\n",determine_rain_likelihood(highest_prob))


if __name__ == "__main__":
    rain = main()
    print(rain)