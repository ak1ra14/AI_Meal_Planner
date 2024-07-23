import streamlit as st
import requests


class GoogleCustomSearch:

    def __init__(self, api_key, search_engine_id):
        self.api_key = api_key
        self.search_engine_id = search_engine_id

    # Web search to obtain links
    def web_search(self, query):
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={self.api_key}&cx={self.search_engine_id}"
        response = requests.get(url)
        results = response.json()
        return results

    def generate_recipe_links(self, food):
        query = f"Recipe for {food}"
        search_results = self.web_search(query)
        print(search_results)
        recipe_links = [
            item['link'] for item in search_results.get('items', [])
        ]
        return recipe_links
