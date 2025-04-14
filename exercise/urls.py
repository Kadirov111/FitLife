from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciseViewSet, WorkoutViewSet

router = DefaultRouter()
router.register(r'exercise', ExerciseViewSet)
router.register(r'workout', WorkoutViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
