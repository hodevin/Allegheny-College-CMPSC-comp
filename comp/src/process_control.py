"""Main file that manages the overall process."""
from data_generation import *
from graphs import *
import pandas as pd


def recreate_city_table(log_file_path, city_table_path):
    """Create a table with city and its respected cases count."""
    df = pd.read_csv(log_file_path)
    # Group the table by city and infections
    grouped_city = df.groupby("City")
    grouped_infection = df.groupby(["City", "Infection"])

    # Initiate new log file.
    header = [
        "City",
        "Mask Policy",
        "Maximum Capacity",
        "Infection Count",
        "Sample Total",
    ]
    with open(city_table_path, "a+") as f:
        input_writer = csv.writer(f, delimiter=",")
        input_writer.writerow(header)

    city_total = []
    # Iterate through each table and append to log.
    for i in grouped_city:
        city_total.append(len(i[1].index))

    id = 0
    for j in grouped_infection:
        elements = []
        if j[0][1] is True:
            elements.append(j[0][0])
            elements.append(j[1].iloc[0]["Mask Policy"])
            elements.append(j[1].iloc[0]["Maximum Capacity"])
            elements.append(len(j[1].index))
            elements.append(city_total[id])
            id += 1

            # Append city status to the log file.
            with open(city_table_path, "a") as f:
                input_writer = csv.writer(f, delimiter=",")
                input_writer.writerow(elements)


def recreate_mask_table(log_file_path, mask_table_path):
    """Create a table with mask policy and its respected cases count."""
    df = pd.read_csv(log_file_path)
    # Group the table by mask policy and infections
    grouped_mask = df.groupby("Mask Policy")
    grouped_infection = df.groupby(["Mask Policy", "Infection"])

    # Initiate new log file.
    header = [
        "Mask Policy",
        "Infection Count",
        "Sample Total",
    ]
    with open(mask_table_path, "a+") as f:
        input_writer = csv.writer(f, delimiter=",")
        input_writer.writerow(header)

    mask_total = []
    # Iterate through each table and append to log.
    for i in grouped_mask:
        mask_total.append(len(i[1].index))

    id = 0
    for j in grouped_infection:
        elements = []
        if j[0][1] is True:
            elements.append(j[0][0])
            elements.append(len(j[1].index))
            elements.append(mask_total[id])
            id += 1

            # Append mask status to the log file.
            with open(mask_table_path, "a") as f:
                input_writer = csv.writer(f, delimiter=",")
                input_writer.writerow(elements)


def recreate_cap_table(log_file_path, cap_table_path):
    """Create a table with capacity policy and its respected cases count."""
    df = pd.read_csv(log_file_path)
    # Group the table by capacity and infections
    grouped_cap = df.groupby("Maximum Capacity")
    grouped_infection = df.groupby(["Maximum Capacity", "Infection"])

    # Initiate new log file.
    header = [
        "Maximum Capacity",
        "Infection Count",
        "Sample Total",
    ]
    with open(cap_table_path, "a+") as f:
        input_writer = csv.writer(f, delimiter=",")
        input_writer.writerow(header)

    cap_total = []
    # Iterate through each table and append to log.
    for i in grouped_cap:
        cap_total.append(len(i[1].index))

    id = 0
    for j in grouped_infection:
        elements = []
        if j[0][1] is True:
            elements.append(j[0][0])
            elements.append(len(j[1].index))
            elements.append(cap_total[id])
            id += 1

            # Append capacity to the log file.
            with open(cap_table_path, "a") as f:
                input_writer = csv.writer(f, delimiter=",")
                input_writer.writerow(elements)


if __name__ == "__main__":
    file_cleaning()
    random_data_generator(1000) # comment this out if using user input data
    # Recreate data table
    recreate_city_table("./data/input_file.csv", "./data/city_table.csv")
    recreate_mask_table("./data/input_file.csv", "./data/mask_table.csv")
    recreate_cap_table("./data/input_file.csv", "./data/cap_table.csv")
    # Graphing
    city_general_graph("./data/city_table.csv")
    mask_graph("./data/mask_table.csv")
    cap_graph("./data/cap_table.csv")
