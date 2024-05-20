country = input("Please add country name: ") # Add country name
visits = int(input("Please input the number of visits: ")) # Number of visits
city_input = input("Give a list of cities you visited seperated by commas: ")
list_of_cities = [city.split() for city in city_input.split(",")] # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.
def add_new_country(country, visits, list_of_cities):
        countries = {"country": country, "visits" : visits, "cities": list_of_cities}
        travel_log.append(countries)


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")