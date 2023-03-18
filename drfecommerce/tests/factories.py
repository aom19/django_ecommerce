import factory

from drfecommerce.product.models import Product, Category, Brand

class CategoryFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Category

	name = factory.Faker('name')
	description = factory.Faker('text')
	created_at = factory.Faker('date_time')



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
	price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True, min_value=0, max_value=10000)

	created_at = factory.Faker('date_time')
	brand = factory.SubFactory(BrandFactory)
	category = factory.SubFactory(CategoryFactory)
