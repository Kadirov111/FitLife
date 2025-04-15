from django.urls import path
from .views import FoodViewSet, MealViewSet

urlpatterns = [
    path('foods/', FoodViewSet.as_view({'get': 'list', 'post': 'create'}), name='food-list'),
    path('meals/', MealViewSet.as_view({'get': 'list', 'post': 'create'}), name='meal-list'),
]
