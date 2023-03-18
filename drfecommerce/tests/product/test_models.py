import pytest

pytestmark = pytest.mark.django_db

class TestCategoryModel:
	def test_str_method(self,category_factory):
		# Arrange
		x = category_factory()

		# Act
		result = str(x)

		# Assert
		# assert result == x.name
		assert x.__str__() == x.name





class TestBrandModel:
	def test_str_method(self,brand_factory):
		x =brand_factory()
		assert x.__str__() == x.name



class TestProductModel:
	def test_str_method(self,product_factory):
		x = product_factory()
		assert x.__str__() == x.name
