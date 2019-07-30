import requests
from django.conf import settings
from django.core.cache import cache
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core import utils
from core.ingredient import IngredientList
from core.recipe import recipe_sites

from api.serializers import IngredientsSerializer


class IndexView(TemplateView):
    template_name = "api/calc_from_text.html"


class AboutView(TemplateView):
    template_name = "api/about.html"

class CalculateFromText(APIView):
    """
    POST Only.
    Calculates nutrition for a user's recipe.

    Parameters:
        :ingredients - List of ingredients
        :servings - (Optional) Number of servings, default 1
    Returns:
        :ingredients - List of ingredients provided by user
        :bad - List of ingredients which couldn't be parsed
        :servings - Number of servings
        :nutrition - list of nutrients
            :name - name of nutrient
                :value - value for whole recipe
                :value_per_serving - value per serving
                :unit - unit of nutrient
    """

    serializer_class = IngredientsSerializer

    def post(self, request):
        """Returns nutritional analysis for recipe"""
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )
        servings = request.data.get("servings", 1)
        user_ingr = request.data.get("ingredients")
        ingredients = IngredientList(user_ingr)
        response_data = {
            "ingredients": user_ingr,
            "bad": ingredients.bad,
            "servings": servings,
            "nutrition": ingredients.total_nutrition(servings),
        }
        return Response(response_data)


class CalculateFromURL(APIView):
    """
    Calculates nutrition for a recipe from a URL.

    Parameters:
        :url - Full URL to recipe
    """

    def post(self, request):
        """
        Returns data about a recipe.
        """
        # TODO: Add proper logging
        # TODO: Move validation to a serializer?
        # Checking if url is valid.
        recipe_url = request.data.get("url", None)
        if not recipe_url:
            return Response(
                {"error": "URL cannot be empty."}, status=status.HTTP_400_BAD_REQUEST
            )
        # If cached, return data
        cached = cache.get(recipe_url, None)
        if cached:
            return Response(cached)
        # Continue validation
        recipe_domain = utils.get_domain_from_url(recipe_url)
        if not recipe_domain in recipe_sites:
            return Response(
                {"error": f"Domain '{recipe_domain}' is not yet supported."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        recipe_request = requests.get(recipe_url)
        if not recipe_request.status_code == 200:
            return Response(
                {
                    "error": f"Site '{recipe_url}' responded with status code: {recipe_request.status_code}"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        parser = recipe_sites[recipe_domain](recipe_request)
        if not parser.is_valid():
            return Response(
                {"error": f"URL '{recipe_url}' is not a valid recipe."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Getting data
        # TODO: Catch exceptions and log them
        parsed = parser.get_data()
        ingredient_list = IngredientList(parsed["ingredients"])
        # Creating response
        response_data = {
            "url": recipe_url,
            "title": parsed["title"],
            "servings": parsed["servings"],
            "total_nutrition": ingredient_list.total_nutrition(parsed["servings"]),
        }
        if settings.DEBUG:
            response_data["ingredients"] = [
                (ing.matched_food.desc_long, ing.weight) for ing in ingredient_list.all
            ]
        # Cache response
        # TODO: Add proper versioning for cache (e.g. version it using MINOR version from Semantic Versioning)
        cache.set(recipe_url, response_data, version=1)
        return Response(response_data)
