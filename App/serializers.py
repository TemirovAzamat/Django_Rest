from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()

    def create(self, validated_data):
        return Category.objects.create(name=validated_data['name'])

    def update(self, instance, validated_data):
        instance.name = validated_data['name']


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.price = validated_data['price']
        instance.category_id = validated_data['category_id']
