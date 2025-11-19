# Garden Advice App
# This app provides gardening tips based on the month and season.

# TODO: Create a function to get the current month
# TODO: Add documentation to all functions
# TODO: Replace hardcoded season names with a dictionary
# TODO: Add error handling for invalid months

month = 5  # Example: May

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