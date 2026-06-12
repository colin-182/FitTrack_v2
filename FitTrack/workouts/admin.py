from django.contrib import admin
from .models import Category, WorkoutPlan, WorkoutLog

admin.site.register(Category)
admin.site.register(WorkoutPlan)
admin.site.register(WorkoutLog)