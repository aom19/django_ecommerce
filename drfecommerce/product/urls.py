from django.urls import path

from . import views


urlpatterns = [
	path('categories/', views.CategoryList.as_view(), name='category-list'),
	path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
	path('brands/', views.BrandList.as_view(), name='product-list'),
	path('brands/<int:pk>/', views.BrandDetail.as_view(), name='product-detail'),

]