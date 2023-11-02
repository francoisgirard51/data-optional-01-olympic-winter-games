# pylint: disable=missing-docstring

import csv

COUNTRIES_FILEPATH = "data/dictionary.csv"
MEDALS_FILEPATH = "data/winter.csv"

def most_decorated_athlete_ever():
    """Returns who won the most winter olympic games medals (gold/silver/bronze) ever"""
    athlete_medal_count = {}

    with open(MEDALS_FILEPATH, mode='r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            athlete = row['Athlete']
            athlete_medal_count[athlete] = athlete_medal_count.get(athlete, 0) + 1

    most_decorated_athlete = max(athlete_medal_count, key=athlete_medal_count.get)
    return most_decorated_athlete

def country_with_most_gold_medals(min_year, max_year):
    """Returns which country won the most gold medals between `min_year` and `max_year`"""
    country_gold_medals = {}
    country_codes = load_country_codes()

    with open(MEDALS_FILEPATH, mode='r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            year = int(row['Year'])
            if min_year <= year <= max_year:
                if row['Medal'] == 'Gold':
                    country_code = row['Country']
                    country = country_codes.get(country_code, None)
                    if country:
                        country_gold_medals[country] = country_gold_medals.get(country, 0) + 1

    most_gold_medals = max(country_gold_medals.values())
    for country, gold_count in country_gold_medals.items():
        if gold_count == most_gold_medals:
            return country
    return None

def load_country_codes():
    """Load the country codes from the dictionary file"""
    country_codes = {}
    with open(COUNTRIES_FILEPATH, mode='r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            country_codes[row['Code']] = row['Country']
    return country_codes

def top_three_women_in_five_thousand_meters():
    """Returns the three women with the most 5000 meters medals(gold/silver/bronze)"""
    athlete_medal_count = {}

    with open(MEDALS_FILEPATH, mode='r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            event = row['Event'].lower()
            gender = row['Gender']
            if '5000m' in event and gender == 'Women':
                athlete = row['Athlete']
                athlete_medal_count[athlete] = athlete_medal_count.get(athlete, 0) + 1

    top_three_athletes = sorted(athlete_medal_count, key=athlete_medal_count.get, reverse=True)[:3]
    return top_three_athletes
