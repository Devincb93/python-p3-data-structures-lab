spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = list()
    for food in spicy_foods:
        names.append(food['name'])
    return names
    

def get_spiciest_foods(spicy_foods):
    spiciest = list()
    for food in spicy_foods:
        if food['heat_level'] > 5:
            spiciest.append(food)
    return spiciest
   

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        heat_level = food["heat_level"]
        origin = food["cuisine"]
        emojis = "🌶" * heat_level
        output = f"{name} ({origin}) | Heat Level: {emojis}"
        print(output)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            name = food['name']
            heat_level = food['heat_level']
            origin = food['cuisine']
            emojis = "🌶" * heat_level
            output = f'{name} ({origin}) | Heat Level: {emojis}'
            print(output)
    

def get_average_heat_level(spicy_foods):
    added_heat_levels = 0
    for food in spicy_foods:
        added_heat_levels += food["heat_level"]
        averaged_heat_levels = added_heat_levels / len(spicy_foods)
    return averaged_heat_levels
    

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_food = spicy_foods.copy()
    new_spicy_food.append(spicy_food)
    return(new_spicy_food)
    pass
