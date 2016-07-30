# -*- coding: utf-8 -*-

# Follow Schema.org
#
# cookTime:             The time it takes to actually cook the dish, in ISO 8601 duration format.
# cookingMethod:         The method of cooking, such as Frying, Steaming, ...
# nutrition:             Nutrition information about the recipe.
# prepTime:             The length of time it takes to prepare the recipe, in ISO 8601 duration format.
# recipeCategory:         The category of the recipe—for example, appetizer, entree, etc.
# recipeCuisine:         The cuisine of the recipe (for example, French or Ethiopian).
# recipeIngredient:     A single ingredient used in the recipe, e.g. sugar, flour or garlic. Supersedes ingredients.
# recipeInstructions:      A step or instruction involved in making the recipe.
# recipeYield:             The quantity produced by the recipe (for example, number of people served, number of servings, etc).
# suitableForDiet:         Indicates a dietary restriction or guideline for which this recipe is suitable, e.g. diabetic, halal etc.
# totalTime:             The total time it takes to prepare and cook the recipe, in ISO 8601 duration format.

import scrapy


class RecipeItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    cookTime = scrapy.Field()
    cookingMethod = scrapy.Field()
    nutrition = scrapy.Field()
    prepTime = scrapy.Field()
    recipeCategory = scrapy.Field()
    recipeCuisine = scrapy.Field()
    recipeIngredient = scrapy.Field()
    recipeInstructions = scrapy.Field()
    recipeYield = scrapy.Field()
    suitableForDiet = scrapy.Field()
    totalTime = scrapy.Field()
