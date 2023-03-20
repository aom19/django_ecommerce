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


class BrandViewSet(viewsets.ViewSet):
	queryset = Brand.objects.all()

	@extend_schema(responses=BrandSerializer)
	def list(self, request):
		serializer = BrandSerializer(self.queryset, many=True)
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




class ProductViewSet(viewsets.ViewSet):
	queryset = Product.objects.all()

	@extend_schema(responses=ProductSerializer)
	def list(self, request):
		serializer = ProductSerializer(self.queryset, many=True)
		return Response(serializer.data)
