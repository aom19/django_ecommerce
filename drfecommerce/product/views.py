from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import status

from .models import Product, Category, Brand
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer


class BrandList(APIView):
	def get(self, request):
		brands = Brand.objects.all()
		serializer = BrandSerializer(brands, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = BrandSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)


class BrandDetail(APIView):
	def get_object(self, pk):
		try:
			return Brand.objects.get(pk=pk)
		except Brand.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def get(self, request, pk):
		brand = self.get_object(pk)
		serializer = BrandSerializer(brand)
		return Response(serializer.data)








class CategoryList(APIView):
	# permission_classes = [IsAuthenticatedOrReadOnly]
	def get(self, request):
		categories = Category.objects.all()
		serializer = CategorySerializer(categories, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = CategorySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)


class CategoryDetail(APIView):
	def get_object(self, pk):
		try:
			return Category.objects.get(pk=pk)
		except Category.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def get(self, request, pk ):
		category = self.get_object(pk)
		serializer = CategorySerializer(category)
		return Response(serializer.data)

	def create(self, request):
		serializer = CategorySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		category = self.get_object(pk)
		serializer = CategorySerializer(category, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ProductList(APIView):
	def get(self, request):
		products = Product.objects.all()
		serializer = ProductSerializer(products, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)

class ProductDetail(APIView):

	def get_object(self, pk):
		try:
			return Product.objects.get(pk=pk)
		except Product.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def get(self, request, pk):
		product = self.get_object(pk)
		serializer = ProductSerializer(product)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		product = self.get_object(pk)
		serializer = ProductSerializer(product, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def delete(self, request, pk, format=None):

		product = self.get_object(pk)
		product.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


