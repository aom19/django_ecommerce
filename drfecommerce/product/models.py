from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
	parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')
	name = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class MPTTMeta:
		order_insertion_by = ['name']

	def __str__(self):
		return self.name




class Brand(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	is_digital = models.BooleanField(default=False)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True)

	# Foreign Keys
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	category = TreeForeignKey(Category, null=True, blank=True ,on_delete=models.CASCADE, related_name='products'),



	def __str__(self):
		return self.name


