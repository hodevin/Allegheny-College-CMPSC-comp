"""Checks user imported data."""

import pandas as pd

print(
    """Testing if the data provided by user matches
the pattern defined by data generator...\n
Please tidy your data if the test does not pass.\n"""
)
# Import data from csv.
df = pd.read_csv("./data/input_file.csv")
group_by_city = df.groupby("City")
group_by_mask = df.groupby("Mask Policy")
group_by_cap = df.groupby("Maximum Capacity")
group_by_infection = df.groupby("Infection")

# Checking the header of csv.
data_header = list(df.columns.values)
header = ["Index", "City", "Mask Policy", "Maximum Capacity", "Infection"]
for h in data_header:
    if h in header:
        print(f"{h} in header.")
    else:
        print(f"{h} not in header.")

# Comparing the total number of cities.
print()
print(f"Total number of cities in generator: {10}")
print(f"Total number of cities provided by user: {len(group_by_city)}\n")

# Check if the cities are in the list defined by generator
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
for city in group_by_city:
    if city[0] in locations:
        print(f"{city[0]}, in list.")
    else:
        print(f"{city[0]}, not in list.")

# Check if mask policy is type boolean.
print()
for mask in group_by_mask:
    if isinstance(mask[0], bool):
        print("Mask Policy is type Boolean.")
    else:
        print("Mask Policy contains non-boolean value.")

# Check if max cap is type boolean.
print()
for cap in group_by_cap:
    if isinstance(cap[0], float):
        print("Maximum Capacity is type float.")
    else:
        print("Maximum Capacity contains non-floating value.")

# Check if infection is type boolean.
print()
for inf in group_by_infection:
    if isinstance(inf[0], bool):
        print("Infection is type Boolean.")
    else:
        print("Infection contains non-Boolean value.")
