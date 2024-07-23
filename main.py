import streamlit as st
import base64
from food_helper import FoodNames
from food_ai_api import FoodAI
from web_search import GoogleCustomSearch
from streamlit_navigation_bar import st_navbar
from edamam import Edamam
from info_helper import InformationHelper
from graph import NutrientGrapher

import os

page = st_navbar(["Casual", "Athletes", "History", "FAQ"])
# if page == "Casual":

OPENAI_API_KEY = os.environ["OPENAI_KEY"]
GOOGLE_SEARCH_API_KEY = os.environ["GOOGLE_SEARCH_API_KEY"]
SEARCH_ENGINE_ID = os.environ["SEARCH_ENGINE_ID"]
EDAMAM_APP_ID = os.environ["EDAMAM_APP_ID"]
EDAMAM_APP_KEY = os.environ["EDAMAM_APP_KEY"]

food_ai = FoodAI(api_key=OPENAI_API_KEY)
fn = FoodNames()
search_recipe_links = GoogleCustomSearch(api_key=GOOGLE_SEARCH_API_KEY, search_engine_id=SEARCH_ENGINE_ID)
edamam_search = Edamam(app_key=EDAMAM_APP_KEY, app_id=EDAMAM_APP_ID)
info_helper = InformationHelper()
nutgraph = NutrientGrapher()

def encode_image(image_path):
    return base64.b64encode(image_path.read()).decode("utf-8")


# ---------------UI-------------------

st.title("Grandma's Cooking AI")

if page == "History":
    recipes = info_helper.get_recipes()

    st.title("Recipe History")
    for recipe in recipes:
        with st.expander(recipe["name"]):
            st.title(recipe["name"])
            st.write("#### Ingredients")
            st.write(recipe["ingredients"])
            st.write("#### Steps")
            st.write(recipe["steps"])

            st.write("#### Filters")
            st.write(f"Preparation Level: {recipe['filters']['prep_level']}")
            st.write(f"Dietary Restrictions: {recipe['filters']['dietary_restrictions']}")
            st.write(f"Cuisine Type: {recipe['filters']['cuisine_choices']}")
            st.write(f"Excluded Foods: {', '.join(recipe['filters']['excluded_foods']) if recipe['filters']['excluded_foods'] != [] else 'None'}")
            nutrients = info_helper.parse_nutrients(recipe["nutrients"])
            nutgraph.plot_nutrient_graph(nutrients)

if page == "Athletes" or page == "Casual":
    athcol1, athcol2, athcol3 = st.columns([1, 1, 1])
    col1, col2 = st.columns([1, 1])
    col4, col5 = st.columns([1, 1])

if page == "Athletes":
    with athcol1:
        cut_bulk = st.selectbox(
            "Cut or Bulk?",
            [
                "Aggressive Cut",
                "Moderate Cut",
                "Maintain",
                "Lean Bulk",
                "Aggressive Bulk",
            ],
        )

    with athcol2:
        prep_level = st.selectbox(
            "Level of Preparation",
            [
                "Easy",
                "Moderate",
                "Difficult",
            ],
            key=["easy", "moderate", "difficult"],
        )

    with athcol3:
        filter_options = st.multiselect("Foods to not include", fn.get_food_names())

        filter_ingredient_string = ", ".join([i for i in filter_options])

if page == "Casual":
    with col1:
        prep_level = st.selectbox(
            "Level of Preparation",
            [
                "Easy",
                "Moderate",
                "Difficult",
            ],
            key=["easy", "moderate", "difficult"],
        )

    with col2:
        filter_options = list(st.multiselect("Foods to not include", fn.get_food_names()))
        filter_ingredient_string = ", ".join([i for i in filter_options])

if page == "Athletes" or page == "Casual":
    with col4:
        dietary_restrictions = st.selectbox(
            "Do you have any dietry restriction?",
            (
                "None",
                "Vegetarian",
                "Vegan",
                "Halal",
                "Lactose intolerant",
                "Gluten intolerant",
                "Custom Option",
            ),
        )

    with col5:
        cuisine_choices = st.selectbox(
            "Cuisine Type:",
            (
                "Any",
                "Thai",
                "Italian",
                "Japanese",
                "Korean",
                "Chinese",
                "Greek",
                "French",
                "Western",
                "Indian",
                "Spanish",
                "American",
                "Galican",
                "Anglo-Indian",
                "Vietnamese",
                "Custom Option",
            ),
        )

    if dietary_restrictions == "Custom Option":
        dietary_restrictions = st.text_input("Enter your custom dietary restriction:")
    if cuisine_choices == "Custom Option":
        cuisine_choices = st.text_input("Enter your custom cuisine type:")

    uploaded_file = st.file_uploader(
        "Upload pictures of past meals (Min 3)", accept_multiple_files=True
    )

if page == "Casual" or page == "Athletes":
    data = None
    generate_recipe = st.button("Generate Recipes")
    if generate_recipe and len(uploaded_file) >= 3:

        if data is None:
            with st.spinner("Generating Recipes..."):
                pass

        image_lst = []
        for i in range(len(uploaded_file)):
            image_lst.append(encode_image(uploaded_file[i]))

        all_ingredients = food_ai.find_ingredients(image_lst)
        data = all_ingredients

        dietary_string = ""
        if dietary_restrictions != "None":
            f"Please return recipes that are suitable for {dietary_restrictions}"

        filters = {"prep_level": prep_level, "dietary_restrictions": dietary_restrictions, "cuisine_choices": cuisine_choices, "excluded_foods" : filter_options}

# ------------------MEAL GENERATION-------------------------

        if data != None:
            st.title(f"{prep_level} Options")
            if page == "Casual":
                easy_meals = food_ai.meal_suggestion(
                    all_ingredients,
                    prep_level,
                    filter_ingredient_string,
                    dietary_restrictions,
                    cuisine_choices,
                )
                data = easy_meals
            elif page == "Athletes":
                easy_meals = food_ai.athlete_meal_suggestion(
                    all_ingredients,
                    prep_level,
                    filter_ingredient_string,
                    dietary_restrictions,
                    cuisine_choices,
                    cut_bulk,
                )
                data = easy_meals

            if "**Ingredients:**" in easy_meals:
                splits = easy_meals.split("###")
            else:
                splits = easy_meals.split("### Meal")

            meal_index = 1
            for meal in splits[1:]:
                if "**Instructions:**" in meal:
                    name, ingredients, recipe = info_helper.new_parse_recipe(meal)
                elif "**Ingredients:**" in meal:
                    name, ingredients, recipe = info_helper.parse_recipe(meal)
                else:
                    name, ingredients, recipe = info_helper.parse_recipe_2nd(meal)  

                links = search_recipe_links.generate_recipe_links(name)

                st.header(name)
                with st.expander(f"View Meal {meal_index} Info"):
                    st.write(meal)

                with st.expander(f"Links to recipes and resources for: {name}"):
                    for i in range(len(links)):
                        st.write(f"{i+1}: {links[i]}")

                ing1 = ingredients.replace(",", "")
                ing = ing1.replace("\n-", ",")[2:]
                array_ingredients = info_helper.ingredient_parser(ing)
                nutrients = edamam_search.get_nutritional_facts_post(array_ingredients)

                with st.expander(f"Meal {meal_index} Nutritional Values"):
                    if "totalNutrients" not in nutrients:
                        break
                    st.write("Nutritional Values")
                    nuts = info_helper.parse_nutrients(nutrients)
                    nutgraph.plot_nutrient_graph(nuts)

                info_helper.insert_recipe(name, ingredients, recipe, nutrients, filters)
                meal_index += 1

# -------------FAQ-------------------
if page == "FAQ":
    with st.expander(f"What if my dietry restriction is not listed in the list?"):
        st.markdown(
            "You may select the **Custom Option** option and enter your custom dietary restriction."
        )

    with st.expander(f"What is 'Athletes?'"):
        st.markdown(
            "Athletes mode provides more tailored and personalised recipes for users who seeks to gain muscle or cut body fat through a combination of high-quality meals."
        )
