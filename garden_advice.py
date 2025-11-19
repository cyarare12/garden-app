# Garden Advice App
# This app provides gardening tips based on the month and season.

import datetime

# TODO: Replace hardcoded season names with a dictionary
# TODO: Add error handling for invalid months

def get_current_month():
    """
    Get the current month as an integer.

    Returns:
        int: The current month (1-12).
    """
    return datetime.datetime.now().month

def get_season(month):
    """
    Determine the season based on the month.

    Args:
        month (int): The month as an integer (1-12).

    Returns:
        str: The season name.
    """
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

def get_vegetables(season):
    """
    Get recommended vegetables for the season.

    Args:
        season (str): The season name.

    Returns:
        str: Comma-separated list of vegetables.
    """
    if season == "Spring":
        return "Carrots, Lettuce, Peas"
    elif season == "Summer":
        return "Tomatoes, Peppers, Cucumbers"
    elif season == "Autumn":
        return "Broccoli, Kale, Spinach"
    else:
        return "Garlic, Onions, Cover crops"

# Main logic
month = get_current_month()
season = get_season(month)
vegetables = get_vegetables(season)

print(f"In {season}, plant these vegetables: ")
print(vegetables)