from unittest.mock import Mock

import pytest
import requests
from django.test import SimpleTestCase

from core.recipe import KwestiaSmaku, RecipeSite, Yummly, recipe_sites


class TestRecipe:
    def test_base_class(self):
        with pytest.raises(NotImplementedError):
            RecipeSite(requests.Request())

    def test_is_recipes_sites_a_dict(self):
        assert isinstance(recipe_sites, dict)

    def test_inherited_class(self):
        class Inherited(RecipeSite):
            pass

        request = requests.Request()
        request.text = r"""<html><body></body></html>"""

        parser = Inherited(request)
        with pytest.raises(NotImplementedError):
            assert parser.get_recipe_title()
        with pytest.raises(NotImplementedError):
            assert parser.get_list_of_ingredients()
        with pytest.raises(NotImplementedError):
            assert parser.get_count_of_servings()
        with pytest.raises(NotImplementedError):
            assert parser.is_valid()

    def test_all_parsers_override_methods(self):

        request = requests.Request()
        request.text = r"<html><body></body></html>"

        for parser in recipe_sites.values():
            try:
                p = parser(request)
                p.get_count_of_servings()
                p.get_data()
                p.get_list_of_ingredients()
                p.get_recipe_title()
            except NotImplementedError:
                pytest.fail(
                    f"Not all parsers override needed methods. ({parser.__name__})"
                )
            except Exception:
                continue

    def test_kwestia_smaku(self):
        request = requests.Request()
        request.text = r"""<html><body>
        <h1 class="przepis page-header">TITLE</h1>
        <div class="field field-name-field-ilosc-porcji field-type-text field-label-hidden">2</div>
        <div class="field field-name-field-skladniki field-type-text-long field-label-hidden">
        <ul>
        <li>150 g chicken breast</li>
        <li>1 red pepper</li></ul>
        </div>
        </body></html>"""

        parser = KwestiaSmaku(request)

        assert parser.get_recipe_title() == "TITLE"
        assert parser.get_count_of_servings() == 2
        assert parser.get_list_of_ingredients() == [
            "150 g chicken breast",
            "1 red pepper",
        ]
        assert parser.is_valid()


class TestYumly(SimpleTestCase):
    def setUp(self):
        self.request = Mock()
        self.request.text = """
        <h1 class="recipe-title">Recipe title</h1>
        <li class="IngredientLine">IngredientLine </li>
        <li class="IngredientLine"> IngredientLine 2</li>
        <div class="servings">
            <input value="2">
        </div>
        """
        self.recipe_site = Yummly(self.request)

    def test_get_list_of_ingredients(self):
        assert self.recipe_site.get_list_of_ingredients() == [
            "IngredientLine",
            "IngredientLine 2",
        ]

    def test_get_count_of_servings(self):
        assert self.recipe_site.get_count_of_servings() == 2

    def test_get_count_of_servings_not_found(self):
        self.request.text = self.request.text.replace('class="servings"', "")
        self.recipe_site = Yummly(self.request)

        assert self.recipe_site.get_count_of_servings() == 1

    def test_is_valid(self):
        assert self.recipe_site.is_valid() is True

    def test_is_valid_not(self):
        self.request.text = self.request.text.replace('class="IngredientLine"', "")
        self.recipe_site = Yummly(self.request)

        assert self.recipe_site.is_valid() is False
