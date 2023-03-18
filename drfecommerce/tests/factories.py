import factory

from drfecommerce.product.models import Product, Category, Brand

class CategoryFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Category

	name = factory.Faker('name')
	description = factory.Faker('text')
	created_at = factory.Faker('date_time')
	
