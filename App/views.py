from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


@api_view(http_method_names=['GET', 'POST'])
def category_list_create_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(instance=categories, many=True)
        return Response(serializer.data, status=201)

    if request.method == 'POST':
        receive_data = request.data
        serializer = CategorySerializer(data=receive_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


@api_view(http_method_names=['GET', 'POST'])
def product_list_create_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(instance=products, many=True)
        return Response(serializer.data, status=201)

    if request.method == 'POST':
        receive_data = request.data
        serializer = ProductSerializer(data=receive_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
