from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from drfecommerce.product import views

router = routers.DefaultRouter()
register = router.register(r'brand', views.BrandViewSet)
register = router.register(r'category', views.CategoryViewSet)
register = router.register(r'product', views.ProductViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls) , name='api'),

]
