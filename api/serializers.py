from rest_framework import serializers


class IngredientsSerializer(serializers.Serializer):
    """Serializer used to validate POST data, but not to return it"""
    ingredients = serializers.ListField(child=serializers.CharField(), allow_empty=False)
    servings = serializers.IntegerField(required=False, min_value=1)
