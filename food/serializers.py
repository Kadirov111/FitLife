from rest_framework import serializers
from .models import Food, Meal, MealFood, HealthMetrics


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class MealFoodSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)
    food_id = serializers.PrimaryKeyRelatedField(
        queryset=Food.objects.all(), source='food', write_only=True
    )

    class Meta:
        model = MealFood
        fields = ['id', 'meal', 'food', 'food_id', 'quantity']


class MealSerializer(serializers.ModelSerializer):
    foods = MealFoodSerializer(source='mealfood_set', many=True, read_only=True)

    class Meta:
        model = Meal
        fields = ['id', 'user', 'date', 'meal_type', 'foods']
        read_only_fields = ['user']


class HealthMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMetrics
        fields = ['id', 'user', 'date', 'weight', 'body_fat_percentage',
                  'blood_pressure_systolic', 'blood_pressure_diastolic', 'heart_rate']
        read_only_fields = ['user']
