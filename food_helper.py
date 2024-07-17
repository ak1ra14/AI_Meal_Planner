import pandas as pd

class FoodNames:

  def __init__(self):
    self.df = pd.read_csv("generic-food.csv")

  def get_food_names(self):
    return list(self.df["FOOD NAME"][:-5])
