from rest_framework import serializers
from .models import Exercise, Workout, WorkoutExercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    exercise_id = serializers.PrimaryKeyRelatedField(
        queryset=Exercise.objects.all(), source='exercise', write_only=True
    )

    class Meta:
        model = WorkoutExercise
        fields = ['id', 'workout', 'exercise', 'exercise_id', 'sets', 'reps', 'weight']


class WorkoutSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseSerializer(source='workoutexercise_set', many=True, read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'user', 'date', 'duration', 'exercises']
        read_only_fields = ['user']
