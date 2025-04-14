from django.db import models
from  users.models import User


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=[('cardio', 'Cardio'), ('strength', 'Strength'), ('flexibility', 'Flexibility'), ('balance', 'Balance')]
    )
    calories_burned_per_hour = models.PositiveIntegerField()


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)