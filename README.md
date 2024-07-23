
# Grandma's Cooking AI (AI Meal Planner)

The AI Meal Planner App is an innovative web application designed to help users maintain a balanced diet by suggesting meals based on their past food photos. By utilizing advanced technologies such as Streamlit, OpenAI API, Edamam API, and Custom Search JSON API, this app provides personalized meal recommendations along with nutritional information.


## Features

**Photo Input:** Users can upload photos of their past meals, which the app analyzes to understand food preferences and dietary habits.

**Meal Suggestions:** Based on the analysis, the app suggests the next possible meal options that align with the user's dietary needs.

**Nutritional Balance:** Each suggested meal comes with detailed nutritional information to help users make informed choices.

**User-Friendly Interface:** Built with Streamlit, the app offers an intuitive and interactive user experience.



## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/ak1ra14/AI-Meal-Planner.git
    cd AI-Meal-Planner
    ```

2. **Install required packages**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up OpenAI API key**
   - Add your OpenAI API key to the Streamlit secrets.
   - Create a `.streamlit/secrets.toml` file and add:
   
     ```toml
     [secrets]
     OPENAI_KEY = "YOUR_OPENAI_API_KEY"
     EDAMAM_APP_ID = "YOUR_EDAMAM_APP_ID"
     EDAMAM_APP_KEY = "YOUR_EDAMAM_APP_KEY"
     GOOGLE_SEARCH_API_KEY = "YOUR_CUSTOM_SEARCH_API_KEY"
     SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE"
     ```
## Usage

Usage
Run the Streamlit app:
```bash
streamlit run main.py
```
1. Select any dietry restrictions if necessary
2. Upload a photo of your past meals.
3. Receive meal suggestions and nutritional information based on your input.

## Demo

Demo and example use cases can be seen from the following link: 
https://www.youtube.com/watch?v=Teu9MsIlIt4





## Badges

![Python](https://a11ybadges.com/badge?logo=python)  
![Replit](https://a11ybadges.com/badge?logo=replit)  
![OpenAI](https://a11ybadges.com/badge?logo=openai)  
![Streamlit](https://a11ybadges.com/badge?logo=streamlit)




## Authors

- [@Aamax-Lee](https://github.com/Aamax-Lee)

- [@Tai Peng](https://github.com/LeeTP03)

- [@Nelson](https://github.com/NelsonTan02)