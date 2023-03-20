import json
import factory
import pytest
from rest_framework import status



class TestCategoryEndpoints:
	endpoint = '/api/category/'
	pytestmark = pytest.mark.django_db


	# def test_get_one_category(self, api_client, category_factory):
	# 	category_factory()
	# 	#act
	# 	response = api_client().get(self.endpoint)
	#
	# 	#assert
	# 	assert response.status_code == 200
	# 	assert len(response.data) == 1

	def test_get_all_categories(self,api_client,category_factory):
		#arrange
		category_factory.create_batch(10)

		response = api_client().get(self.endpoint)

		assert response.status_code == status.HTTP_200_OK
		assert len(response.json()) == 10





class TestBrandEndpoints:
	endpoint = '/api/brand/'
	pytestmark = pytest.mark.django_db


	def test_get_all_brands(self, api_client, brand_factory):
		brand_factory.create_batch(10)

		response = api_client().get(self.endpoint)

		assert response.status_code == 200
		assert len(response.data) == 10

	# def test_get_one_brand(self, api_client, brand_factory):
	# 	brand_factory()
	# 	response = api_client().get(self.endpoint)
	#
	# 	assert response.status_code == 200
	# 	assert len(response.data) == 1




class TestProductEndpoints:
	endpoint = '/api/product/'
	pytestmark = pytest.mark.django_db

	def test_get_all_products(self, api_client, product_factory):
		product_factory.create_batch(10)

		response = api_client().get(self.endpoint)

		assert response.status_code == 200
		assert len(response.data) == 10







