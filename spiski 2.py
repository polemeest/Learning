countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}
count = ''
city = input()
for country, gorod in countries.items():
    if city in gorod:
        count = country
        break
print(f'INFO: {city} is a city in {count}' if count != '' else f'ERROR: Country for {city} not found')



countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()
country = [k for k, v in countries.items() if city in v]
print(f'INFO: {city} is a city in {country[0]}' if country else f'ERROR: Country for {city} not found')