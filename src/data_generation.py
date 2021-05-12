"""Data generator."""
import random
import shutil
import csv
import os


def file_cleaning():
    """Clear the previous version of data if needed."""
    # Create data dir if not existed.
    if os.path.exists("./data"):
        shutil.rmtree("./data")
        os.mkdir("./data")
    else:
        os.mkdir("./data")


def random_data_generator(user_amount):
    """Generate random COVID-19 data. For experimental projects use only."""
    # Write a header to the csv file.
    header = ["Index", "City", "Mask Policy", "Maximum Capacity", "Infection"]
    with open("data/input_file.csv", mode="a+") as input_file:
        input_writer = csv.writer(input_file, delimiter=",")
        input_writer.writerow(header)

    # Generate random percentage of the capacity limit for each city.
    locations = [
        "Anchorage",
        "Pittsburgh",
        "Baltimor",
        "Houston",
        "New York",
        "Los Angeles",
        "Miami",
        "Boston",
        "Saint Louis",
        "Denver",
    ]
    capacity_percentages = [0.25, 0.50, 0.75, 1.00]

    # Assign capacity.
    percentage_rule = {}
    for i in locations:
        capacity = random.choice(capacity_percentages)
        percentage_rule[i] = capacity

    # Generate index for each user in the range defined.
    for x in range(user_amount):
        elements = []
        userid = x + 1
        elements.append(str(userid))
        # print(elements)
        # Randomly assign a location to the person.
        city = random.choice(locations)
        elements.append(str(city))
        # print(elements)
        # Randomly determine mask mandate (boolean).
        city_mask = [
            "Anchorage",
            "Baltimor",
            "Houston",
            "Miami",
            "Saint Louis",
            "Denver",
        ]
        if city in city_mask:
            elements.append("True")
        else:
            elements.append("False")
        # print(elements)
        # Match city to the capacity.
        elements.append(percentage_rule[city])
        # print(elements)
        # Generate random boolean for COVID-19.
        covid_result = bool(random.getrandbits(1))
        elements.append(str(covid_result))
        # print(elements)

        # Write data into a log file.
        with open("data/input_file.csv", mode="a") as input_file:
            input_writer = csv.writer(input_file, delimiter=",")
            input_writer.writerow(elements)
