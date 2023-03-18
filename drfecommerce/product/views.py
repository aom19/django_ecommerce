from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response


from .models import Product , Category , Brand
from .serializers import ProductSerializer , CategorySerializer , BrandSerializer


class BrandViewSet(viewsets.ViewSet):
	queryset = Brand.objects.all()

	def list(self, request):
		serializer = BrandSerializer(self.queryset, many=True)
		return Response(serializer.data)


class CategoryViewSet(viewsets.ViewSet):
	queryset = Category.objects.all()

	def list(self, request):
		serializer = CategorySerializer(self.queryset, many=True)
		return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
	queryset = Product.objects.all()

	def list(self, request):
		serializer = ProductSerializer(self.queryset, many=True)
		return Response(serializer.data)


