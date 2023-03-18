from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from drfecommerce.product import views


router = routers.DefaultRouter()
router.register(r'brand', views.BrandViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ProductViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls) , name='api'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),


]
