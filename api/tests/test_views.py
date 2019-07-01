import pytest
from django.core.cache import cache
from django.shortcuts import reverse
from rest_framework.test import APIClient
from core.recipe import recipe_sites

client = APIClient()


@pytest.mark.django_db
def test_no_url_error():
    response = client.post(reverse("calculate-from-url"), {}, format="json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_domain_not_supported():
    response = client.post(
        reverse("calculate-from-url"),
        {"url": "http://notsupportedsite.org"},
        format="json",
    )
    assert response.status_code == 400


@pytest.mark.django_db
def test_supported_but_bad_response():
    response = client.post(
        reverse("calculate-from-url"),
        {"url": "https://www.kwestiasmaku.com/recipe-doesnt-exist"},
        format="json",
    )
    assert response.status_code == 400


@pytest.mark.django_db
def valid_url_but_no_recipe():
    response = client.post(
        reverse("calculate-from-url"),
        {"url": "https://www.kwestiasmaku.com/"},
        format="json",
    )
    assert response.status_code == 400


@pytest.mark.django_db
def test_cache(settings):
    # This test will fail with dummy backend.
    # if settings.CACHES['default']['BACKEND'] == "django.core.cache.backends.dummy.DummyCache":
    #     return
    url = "https://www.kwestiasmaku.com/przepis/kurczak-slodko-kwasny"
    cache.delete(url)
    response = client.post(reverse("calculate-from-url"), {"url": url}, format="json")
    assert response.status_code == 200
    assert cache.get(url) is not None


@pytest.mark.django_db
class TestCalculateFromTextApiView:
    url = reverse("calculate-from-text")
    client = APIClient()

    def test_return_400_when_invalid_ingredients(self):
        """Ensure that view returns HTTP 400 when given invalid ingredients parameter"""
        # blank ingredients
        response = self.client.post(self.url, {})
        assert response.status_code == 400
        # integer (not a string or array-like)
        response = self.client.post(self.url, {"ingredients": 5}, format="json")
        assert response.status_code == 400

    def test_return_400_when_invalid_servings(self):
        """Ensure that view returns HTTP 400 when given invalid servings parameter"""
        # lower than 1
        response = self.client.post(self.url, {"ingredients": "abc", "servings": 0}, format="json")
        assert response.status_code == 400
        # not an integer
        response = self.client.post(self.url, {"ingredients": "abc", "servings": 1.5}, format="json")
        assert response.status_code == 400
    
    def test_return_200_when_valid_ingredients(self):
        """Ensure that view can return HTTP 200 when given valid ingredients"""
        # string
        response = self.client.post(self.url, {"ingredients": "abc"}, format="json")
        assert response.status_code == 200
        # list
        response = self.client.post(self.url, {"ingredients": ["abc"]}, format="json")
        assert response.status_code == 200
        # tuple
        response = self.client.post(self.url, {"ingredients": ("abc",)}, format="json")
        assert response.status_code == 200
    
    def test_view_splits_ingredients_correctly(self):
        """Ensure that ingredients are split according to the type"""
        # string
        response = self.client.post(self.url, {"ingredients": "abc\ndef"}, format="json")
        assert response.data["ingredients"] == ["abc", "def"]
        # list
        response = self.client.post(self.url, {"ingredients": ["abc", "def"]}, format="json")
        assert response.data["ingredients"] == ["abc", "def"]
        # tuple
        response = self.client.post(self.url, {"ingredients": ("abc", "def")}, format="json")
        assert response.data["ingredients"] == ["abc", "def"]