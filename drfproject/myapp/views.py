from rest_framework import generics, viewsets
from django.shortcuts import render
from .models import CategoriesOfProducts
from .serializers import CategoriesOfProductsSerializer


class MyappViewset(viewsets.ModelViewSet):
    queryset = CategoriesOfProducts.objects.all()
    serializer_class = CategoriesOfProductsSerializer


# class MyappAPIList(generics.ListCreateAPIView):
#     queryset = CategoriesOfProducts.objects.all()
#     serializer_class = CategoriesOfProductsSerializer
#
#
# class MyappAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CategoriesOfProducts.objects.all()
#     serializer_class = CategoriesOfProductsSerializer


