
from django.db import models
from django.contrib.auth.models import User


# =====================================
# RESTAURANT MODEL
# =====================================

class Restaurant(models.Model):

    name = models.CharField(max_length=200)
    address = models.TextField()
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=100, blank=True)

    image = models.ImageField(
        upload_to='restaurants/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


# =====================================
# FOOD ITEM MODEL
# =====================================

class FoodItem(models.Model):

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='food_items'
    )

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    category = models.CharField(max_length=100)

    calories = models.PositiveIntegerField(default=0)

    image = models.ImageField(
        upload_to='food_items/',
        blank=True,
        null=True
    )

    is_vegetarian = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# =====================================
# NUTRITION PROFILE MODEL
# =====================================

class NutritionProfile(models.Model):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    ACTIVITY_CHOICES = [
        ('sedentary', 'Little or no exercise'),
        ('light', 'Light exercise (1-3 days/week)'),
        ('moderate', 'Moderate exercise (3-5 days/week)'),
        ('active', 'Heavy exercise (6-7 days/week)'),
        ('very_active', 'Very heavy exercise'),
    ]

    DIET_CHOICES = [
        ('vegetarian', 'Vegetarian'),
        ('non_vegetarian', 'Non-Vegetarian'),
        ('both', 'Both'),
    ]

    GOAL_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('weight_gain', 'Weight Gain'),
        ('muscle_gain', 'Muscle Gain'),
        ('maintain', 'Maintain Weight'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='nutrition_profile'
    )

    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    height = models.FloatField(
        help_text='Height in centimeters'
    )

    weight = models.FloatField(
        help_text='Weight in kilograms'
    )

    activity_level = models.CharField(
        max_length=20,
        choices=ACTIVITY_CHOICES
    )

    diet_preference = models.CharField(
        max_length=20,
        choices=DIET_CHOICES,
        default='both'
    )

    goal = models.CharField(
        max_length=20,
        choices=GOAL_CHOICES,
        default='weight_loss'
    )

    allergies = models.TextField(blank=True)

    medical_restrictions = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - Nutrition Profile'
