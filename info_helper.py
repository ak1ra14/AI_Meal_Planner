
import requests
import json
import re


class InformationHelper:
    def __init__(self):
        self.url = "https://sadly-oriented-husky.ngrok-free.app/recipes"

    def get_recipes(self):
        response = requests.get(self.url)
        return response.json()

    def parse_recipe(self, recipe):
        name = recipe.split(":")[1].split("**")[0]
        if name == "":
            name = recipe.split(":")[0].split("**")[0]

        ingredients = recipe.split("**Ingredients:**")[1].split("**Recipe:**")[0]
        recipe = recipe.split("**Recipe:**")[1]

        return name, ingredients, recipe

    def parse_recipe_2nd(self, meal):
        parts = meal.split("####")
        name = parts[0][3:]
        ingredients = parts[2].replace("Ingredients:", "")
        steps = parts[3].replace("Recipe:", "")
        return name, ingredients, steps

    def new_parse_recipe(self, meal):
        name = meal.split(":")[1].split("**")[0]
        ingredients = meal.split("**Ingredients:**")[1].split("**Instructions:**")[0]
        recipe = meal.split("**Instructions:**")[1]

        return name, ingredients, recipe

    def insert_recipe(self, name, ingredients, steps, nutrients, filters):
        data = {
            "name": name,
            "ingredients": ingredients,
            "steps": steps,
            "nutrients": nutrients,
            "filters": filters,
        }

        response = requests.post(self.url, json=data)
        return response.json()

    def ingredient_parser(self, ingredients):
        next_text = ingredients.replace("\n", "")
        new_text = re.sub(r"\([^()]*\)", "", next_text)
        return new_text.split(",")

    def parse_nutrients(self, nutrients):
        main = [
            "ENERC_KCAL",
            "FAT",
            "FASAT",
            "FATRN",
            "CHOCDF",
            "FIBTG",
            "SUGAR",
            "PROCNT",
            "CHOLE",
            "NA",
            "CA",
            "FE",
            "VITA_RAE",
            "VITC",
        ]
        lst = [
            "ENERC_KCAL",
            "FAT",
            "FASAT",
            "FATRN",
            "FAMS",
            "FAPU",
            "CHOCDF",
            "FIBTG",
            "SUGAR",
            "PROCNT",
            "CHOLE",
            "NA",
            "CA",
            "MG",
            "K",
            "FE",
            "ZN",
            "P",
            "VITA_RAE",
            "VITC",
            "THIA",
            "RIBF",
            "NIA",
            "VITB6A",
            "FOLDFE",
            "VITB12",
            "VITD",
            "TOCPHA",
            "VITK1",
            "WATER",
        ]

        nutdict = {
            "Nutrient": [
                nutrients["totalNutrients"][nutcode]["label"] for nutcode in main
            ],
            "Amount": [
                nutrients["totalNutrients"][nutcode]["quantity"] for nutcode in main
            ],
            "Unit": [nutrients["totalNutrients"][nutcode]["unit"] for nutcode in main],
            "Daily Value": [
                (
                    nutrients["totalDaily"][nutcode]["quantity"]
                    if nutcode not in ["FATRN", "SUGAR"]
                    else 0
                )
                for nutcode in main
            ],
            "Type": [
                (
                    "Macro"
                    if nutcode
                    in [
                        "ENERC_KCAL",
                        "FAT",
                        "FASAT",
                        "FATRN",
                        "CHOCDF",
                        "FIBTG",
                        "SUGAR",
                        "PROCNT",
                    ]
                    else "Micro"
                )
                for nutcode in main
            ],
        }

        return nutdict
