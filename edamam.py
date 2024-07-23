import requests
import os

class Edamam():
    def __init__(self, app_key, app_id) -> None:
        self.app_key = app_key
        self.app_id = app_id

    def get_nutritional_facts(self, ingredients): 
        result = requests.get(
            f"https://api.edamam.com/api/nutrition-data?app_id={self.app_id}&app_key={self.app_key}&nutrition-type=cooking&ingr={ingredients}"
        )

        data = result.json()
        return data

    def get_nutritional_facts_post(self, ingredients): 
        result = requests.post(
            f"https://api.edamam.com/api/nutrition-details?app_id={self.app_id}&app_key={self.app_key}",
            json={
                "title": "Chicken Quinoa",
                "ingr": ingredients,
                "url": "https://youtube.com/",
                "summary": "string",
                "yield": "string",
                "time": "string",
                "img": "string",
                "prep": "string"
            }
        )
        return result.json()