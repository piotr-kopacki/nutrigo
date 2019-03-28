from django.db.transaction import atomic

from core.models import FoodWeight


@atomic
def correct():
    for weight in FoodWeight.objects.filter(amount=0.0):
        weight.amount = 1.0
        weight.save()
