import requests
from bs4 import BeautifulSoup

from core import ingredient, utils


class RecipeSite:
    """Base class for RecipeSite (parser).

    Attributes:
    :language - language of recipe, default: "en"
    :request - request object from requests library.
    :soup - BeatifulSoup object initialized with request and lxml parser. Use it to find elements in HTML.

    You need to override these methods:
        - get_recipe_title()
        - get_list_of_ingredients()
        - get_count_of_servings()
    """
    language = "en"

    def __init__(self, request: requests.request):
        if self.__class__ is RecipeSite:
            raise NotImplementedError(
                "Do not initialize this class. Inherit from it, instead."
            )
        self.request = request
        self.soup = BeautifulSoup(request.text, "lxml")

    def get_data(self) -> dict:
        """Returns title, servings and ingredients of a recipe.

        Returns:
            Dictionary with title, servings and list of Ingredient objects
            {
                'title': 'Recipe name',
                'servings': 1,
                'ingredients': [
                    'chicken breast',
                    ...
                ]
            }
        """
        title = self.get_recipe_title()
        servings = self.get_count_of_servings()
        ingredients = (
            self.get_list_of_ingredients()
            if self.language == "en"
            else utils.translate_many(self.get_list_of_ingredients())
        )
        return {
            "title": title,
            "servings": servings,
            "ingredients": ingredients,
        }

    def get_recipe_title(self) -> str:
        """This method should return recipe title by parsing request."""
        raise NotImplementedError("Override this method.")

    def get_list_of_ingredients(self) -> list:
        """This method should return list of ingredients by parsing request."""
        raise NotImplementedError("Override this method.")

    def get_count_of_servings(self) -> int:
        """This method should return count of servings by parsing request (1 by default)."""
        raise NotImplementedError("Override this method.")

    def is_valid(self) -> bool:
        """This method should validate request."""
        raise NotImplementedError("Override this method.")


class KwestiaSmaku(RecipeSite):
    language = "pl"

    def get_recipe_title(self):
        title = self.soup.find("h1", {"class": "przepis page-header"})
        return title.get_text().strip()

    def get_list_of_ingredients(self):
        ingredients_div = self.soup.find(
            "div",
            "field field-name-field-skladniki field-type-text-long field-label-hidden",
        )
        ingredient_list = ingredients_div.find_all("li")
        return [ing.get_text().strip() for ing in ingredient_list]

    def get_count_of_servings(self):
        servings_div = self.soup.find(
            "div",
            "field field-name-field-ilosc-porcji field-type-text field-label-hidden",
        )
        if servings_div:
            for w in servings_div.get_text().strip().split(" "):
                if w.isnumeric():
                    return int(w)
        return 1

    def is_valid(self):
        ingredients_div = self.soup.find(
            "div",
            "field field-name-field-skladniki field-type-text-long field-label-hidden",
        )
        return bool(ingredients_div)


class Yummly(RecipeSite):
    def get_recipe_title(self):
        title = self.soup.find("h1", {"class": "recipe-title"})
        return title.get_text().strip()

    def get_list_of_ingredients(self):
        ingredient_list = self.soup.find_all("li", {"class": "IngredientLine"})
        return [ing.get_text().strip() for ing in ingredient_list]

    def get_count_of_servings(self):
        servings = self.soup.find("div", {"class": "servings"})
        if servings:
            return int(servings.find("input")["value"])
        return 1

    def is_valid(self):
        ingredient_list = self.soup.find_all("li", {"class": "IngredientLine"})
        return bool(ingredient_list)        


recipe_sites = {
    "kwestiasmaku.com": KwestiaSmaku,
    "yummly.com": Yummly,
}
