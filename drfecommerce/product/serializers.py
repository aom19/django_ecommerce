from rest_framework     import serializers
from drfecommerce.product.models import Product, Brand, Category


class BrandSerializer(serializers.ModelSerializer):
	class Meta:
		model = Brand
		fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
	brand = BrandSerializer()
	category = CategorySerializer()

	class Meta:
		model = Product
		fields = '__all__'

