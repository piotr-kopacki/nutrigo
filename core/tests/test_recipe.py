import pytest
import requests

from core.recipe import KwestiaSmaku, RecipeSite, recipe_sites


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
                pytest.fail(f"Not all parsers override needed methods. ({parser.__name__})")
            except:
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
            "1 red pepper"
        ]
        assert parser.is_valid()
