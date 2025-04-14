from django.contrib import admin
from .models import Exercise, Workout, WorkoutExercise

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'calories_burned_per_hour']
    search_fields = ['name', 'category']

class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'duration']
    inlines = [WorkoutExerciseInline]
