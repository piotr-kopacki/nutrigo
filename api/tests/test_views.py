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


def test_recipe_websites_view(client):
    data = client.get(reverse('recipe-websites-view'))
    assert data.context['supported_websites'] == recipe_sites.keys()