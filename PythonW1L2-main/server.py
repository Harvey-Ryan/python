from models.weather import Weather
import time


Weather.save({
    "city":"Dallas",
    "state":"TX",
    "temp":"68",
    "precip":"40%"
})

Weather.save({
    "city":"Dallas",
    "state":"TX",
    "temp":"68",
    "precip":"40%"
})

Weather.save({
    "city":"Concord",
    "state":"CA",
    "temp":"47",
    "precip":"100%"
})

Weather.save({
    "city":"Joplin",
    "state":"MO",
    "temp":"45",
    "precip":"15%"
})

Weather.save({
    "city":"Milpitas",
    "state":"CA",
    "temp":"51",
    "precip":"100%"
})

Weather.save({
    "city":"Philadelphia",
    "state":"PA",
    "temp":"45",
    "precip":"50%"
})

Weather.save({
    "city":"Los Angeles",
    "state":"CA",
    "temp":"59",
    "precip":"0%"
})

Weather.save({
    "city":"Boiling Springs",
    "state":"PA",
    "temp":"42",
    "precip":"20%"
})

Weather.save({
    "city":"Phoenix",
    "state":"AZ",
    "temp":"69",
    "precip":"0%"
})


def weatherBot():
    print("Would you like to know the weather from a specific city?")
    user_input = input()
    if user_input == "y":
        print("What city weather would you like to know?")
        print("Here is a list of available cities")
        for x in Weather.get_all():
            print(x.city)
        city = input()
        this_weather = Weather.get_one_by_city(city)
        print(f"The temperature in {this_weather.city} is {this_weather.temp}, the chance of rain is {this_weather.precip}.")
    elif user_input == "n":
        print("Ok")
    else:
        print("Invalid")


weatherBot()