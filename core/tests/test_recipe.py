from core.recipe import RecipeSite, recipe_sites

import pytest
import requests

class TestRecipe:
    def test_base_class(self):
        with pytest.raises(NotImplementedError):
            r = RecipeSite(requests.Request())
    
    def test_is_recipes_sites_a_dict(self):
        assert isinstance(recipe_sites, dict)

    def test_inherited_class(self):
        class Inherited(RecipeSite):
            pass
        
        request = requests.Request()
        request.text = r"<html><body></body></html>"

        parser = Inherited(request)
        with pytest.raises(NotImplementedError):
            assert parser.get_recipe_title()
        with pytest.raises(NotImplementedError):
            assert parser.get_list_of_ingredients()
        with pytest.raises(NotImplementedError):
            assert not parser.get_count_of_servings()

        
            