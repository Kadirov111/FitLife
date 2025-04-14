from django.contrib import admin
from .models import Food, Meal, MealFood, HealthMetrics

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'calories', 'protein', 'carbs', 'fats']
    search_fields = ['name']

class MealFoodInline(admin.TabularInline):
    model = MealFood
    extra = 1

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'meal_type']
    inlines = [MealFoodInline]

@admin.register(HealthMetrics)
class HealthMetricsAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'weight', 'body_fat_percentage', 'heart_rate']
