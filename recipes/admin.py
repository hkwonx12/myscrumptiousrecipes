from django.contrib import admin
from .models import Recipe, RecipeStep, Ingredient
# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_on",
        "id"
    )

@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = (
        "step_number",
        "recipe_title",
        "id",
    )

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "amount",
        "food_item",
        "id", 
    )
