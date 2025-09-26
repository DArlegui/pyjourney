def get_formatted_location(city, country, population):
    formatted_location = f"{city} {country} {population}"
    return formatted_location.title()


def get_formatted_location_default(city, country, population=3_500_000):
    formatted_location = f"{city} {country} {population}"
    return formatted_location.title()
