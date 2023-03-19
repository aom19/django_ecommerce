import pytest
from drfecommerce.product.models import Product, Category, Brand

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

	def test_category_model(self,category_factory):
		# Create a parent category
		parent_category = Category.objects.create(name='Parent Category')

		# Create a child category
		child_category = Category.objects.create(name='Child Category', parent=parent_category)

		# Check if the child category is a child of the parent category
		assert child_category.get_parent() == parent_category

		# Check if the child category is a leaf node






class TestBrandModel:
	def test_str_method(self,brand_factory):
		x =brand_factory()
		assert x.__str__() == x.name



class TestProductModel:
	def test_str_method(self,product_factory):
		x = product_factory()
		assert x.__str__() == x.name
