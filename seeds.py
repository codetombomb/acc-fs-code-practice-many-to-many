from models import Recipe, Ingredient
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data.db")
Session = sessionmaker(bind=engine)
session = Session()

# For generating Fake data: https://faker.readthedocs.io/en/master/providers.html
# from faker import Faker

session.query(Recipe).delete()
session.query(Ingredient).delete()

# For working with an API and retrieving json data
import requests
import json
import random

alphabet_lowercase = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "v",
    "w",
    "y",
]
MEAL_API_SEARCH_URL_BASE = "https://www.themealdb.com/api/json/v1/1/search.php?f="

for letter in alphabet_lowercase:
    response = requests.get(MEAL_API_SEARCH_URL_BASE + letter)
    json_data = json.loads(response.text)
    for meal in json_data["meals"]:
        recipe = Recipe(
            name=meal["strMeal"],
            category=meal["strCategory"],
            instructions=meal["strInstructions"],
            area=meal["strArea"]
        )

        session.add(recipe)
        session.commit()

        for num in range(1,20):
            ingredient_key = f"strIngredient{num}"
            if meal[ingredient_key] and not Ingredient.find_by(meal[ingredient_key]):
                
                ingredient = Ingredient(name=meal[ingredient_key])
                
                session.add(ingredient)
                session.commit()
                
import ipdb;ipdb.set_trace()
