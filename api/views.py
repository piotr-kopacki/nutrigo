import requests
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from core import utils
from core.ingredient import (Ingredient, IngredientError,
                             calculate_serving_nutrition,
                             calculate_total_nutrition)
from core.recipe import recipe_sites


class IndexView(TemplateView):
    template_name = "api/index.html"


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
        # TODO: Add caching
        # TODO: Move validation to a serializer?
        # Checking if url is valid.
        recipe_url = request.data.get("url", None)
        if not recipe_url:
            return Response(
                {"error": "URL cannot be empty."},
                status=status.HTTP_400_BAD_REQUEST,
            )
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
                {
                    "error": f"URL '{recipe_url}' is not a valid recipe."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Getting data
        # TODO: Catch exceptions and log them
        parsed = parser.get_data()
        total_nutrition = calculate_total_nutrition(parsed['ingredients'])
        serving_nutrition = calculate_serving_nutrition(total_nutrition, parsed['servings'])
        # Creating response
        response = {
            'url': recipe_url,
            'title': parsed['title'],
            'servings': parsed['servings'],
            'total_nutrition': total_nutrition,
            'serving_nutrition': serving_nutrition,
            'ingredients': [(ing.name, ing.weight, ing.matched_food.desc_long) for ing in parsed['ingredients']], # delete dis
        }
        return Response(response)
