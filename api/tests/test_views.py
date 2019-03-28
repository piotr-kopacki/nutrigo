import pytest
from django.shortcuts import reverse
from rest_framework.test import APIClient

client = APIClient()

def test_no_url_error():
    response = client.post(reverse('calculate-from-url'), {}, format='json')
    assert response.status_code == 400

def test_domain_not_supported():
    response = client.post(reverse('calculate-from-url'), {"url": "http://notsupportedsite.org"}, format='json')
    assert response.status_code == 400

def test_supported_but_bad_response():
    response = client.post(reverse('calculate-from-url'), {"url": "https://www.kwestiasmaku.com/recipe-doesnt-exist"}, format='json')
    assert response.status_code == 400

def valid_url_but_no_recipe():
    response = client.post(reverse('calculate-from-url'), {"url": "https://www.kwestiasmaku.com/"}, format='json')
    assert response.status_code == 400
