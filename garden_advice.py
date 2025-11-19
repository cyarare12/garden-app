# Garden Advice App
# This app provides gardening tips based on the month and season.

import datetime

# TODO: Add documentation to all functions
# TODO: Replace hardcoded season names with a dictionary
# TODO: Add error handling for invalid months

def get_current_month():
    """Get the current month as an integer."""
    return datetime.datetime.now().month

month = get_current_month()

if month in [12, 1, 2]:
    season = "Winter"
elif month in [3, 4, 5]:
    season = "Spring"
elif month in [6, 7, 8]:
    season = "Summer"
else:
    season = "Autumn"

print(f"In {season}, plant these vegetables: ")

if season == "Spring":
    print("Carrots, Lettuce, Peas")
elif season == "Summer":
    print("Tomatoes, Peppers, Cucumbers")
elif season == "Autumn":
    print("Broccoli, Kale, Spinach")
else:
    print("Garlic, Onions, Cover crops")