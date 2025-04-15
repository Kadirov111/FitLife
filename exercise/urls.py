from django.urls import path
from .views import ExerciseViewSet, WorkoutViewSet

urlpatterns = [
    path('exercises/', ExerciseViewSet.as_view({'get': 'list', 'post': 'create'}), name='exercise-list'),
    path('workouts/', WorkoutViewSet.as_view({'get': 'list', 'post': 'create'}), name='workout-list'),
]
