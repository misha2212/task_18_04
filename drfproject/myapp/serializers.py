from rest_framework import serializers

from .models import CategoriesOfProducts


class CategoriesOfProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesOfProducts
        fields = '__all__'
