
from django.contrib import admin
from .models import Restaurant, FoodItem


class FoodItemInline(admin.TabularInline):
    model = FoodItem
    extra = 1


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone')
    search_fields = ('name', 'city')
    inlines = [FoodItemInline]


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'restaurant',
        'category',
        'price',
        'is_vegetarian',
        'is_available'
    )

    list_filter = (
        'category',
        'is_vegetarian',
        'is_available'
    )

    search_fields = ('name', 'restaurant__name')

from .models import NutritionProfile

@admin.register(NutritionProfile)
class NutritionProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'age',
        'gender',
        'height',
        'weight',
        'activity_level',
        'diet_preference',
        'goal',
    )
