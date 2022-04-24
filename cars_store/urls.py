from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from cars.views import CarDealerViewSet, CarViewSet, ApplicationViewSet

router = routers.SimpleRouter()
router.register(r'dealers', CarDealerViewSet)
router.register(r'cars', CarViewSet)
router.register(r'application', ApplicationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
]
