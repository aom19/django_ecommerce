import factory
from factory.django import DjangoModelFactory
from drfecommerce.product.models import Product, Category, Brand

class CategoryFactory(DjangoModelFactory):
	class Meta:
		model = Category


	name = factory.Faker('word')
	description = factory.Faker('sentence')
	created_at = factory.Faker('date_time')
	parent=  factory.SubFactory('drfecommerce.tests.factories.CategoryFactory', parent=None)



class BrandFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Brand

	name = factory.Faker('name')
	description = factory.Faker('text')
	created_at = factory.Faker('date_time')



class ProductFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Product

	name = factory.Faker('name')
	description = factory.Faker('text')
	is_digital = factory.Faker('boolean')
	price = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True, min_value=10, max_value=100)
	created_at = factory.Faker('date_time')
	brand = factory.SubFactory(BrandFactory)
	category = factory.SubFactory(CategoryFactory)
