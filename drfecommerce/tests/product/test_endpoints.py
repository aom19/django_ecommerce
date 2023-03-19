import json
import factory
import pytest


class TestCategoryEndpoints:
	endpoint = '/api/category/'
	pytestmark = pytest.mark.django_db


	def test_get_one_category(self, api_client, category_factory):
		category_factory()

		#act
		response = api_client().get(self.endpoint)

		#assert
		assert response.status_code == 200
		assert len(response.data) == 1

	# def test_get_all_categories(self, api_client, category_factory):
	# 	# Arrange
	# 	category_factory.create_batch(3)
	#
	# 	# Act
	# 	response = api_client.get(self.endpoint)
	#
	# 	# Assert
	# 	assert response.status_code == 200
	# 	assert len(response.json()) == 3





class TestBrandEndpoints:
	endpoint = '/api/brand/'
	pytestmark = pytest.mark.django_db


	def test_get_one_brand(self, api_client, brand_factory):
		brand_factory()
		response = api_client().get(self.endpoint)
		assert response.status_code == 200
		assert len(response.data) == 1


	def test_get_all_brands(self, api_client, brand_factory):
		brand_factory.create_batch(3)
		response = api_client().get(self.endpoint)
		print(json.loads(response.content))
		assert response.status_code == 200
		assert len(json.loads(response.content)) == 3



class TestProductEndpoints:
	pass




