from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodViewSet, MealViewSet, HealthMetricsViewSet

router = DefaultRouter()
router.register(r'food', FoodViewSet)
router.register(r'meal', MealViewSet)
router.register(r'health-metrics', HealthMetricsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
