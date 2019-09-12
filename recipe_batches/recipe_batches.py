#!/usr/bin/python

import math

rec = { 'milk': 2 }
ingr =  { 'milk': 200}

def recipe_batches(recipe, ingredients):
  total_number_batches = 0
  # determine whether or not all ingredients are present
  if len(recipe) != len(ingredients):
    return 0
  for k in recipe and ingredients:
    if len(recipe) == 1 and len(ingredients) == 1:
      total_number_batches = round(ingredients[k]/recipe[k])
    if recipe[k] > ingredients[k]:
      total_number_batches = 0
    if recipe[k] < ingredients[k] or recipe[k] == ingredients[k]:
        result = ingredients[k]/recipe[k]
        for key in recipe and ingredients:
          if ingredients[key]/recipe[key] < result:
            result = ingredients[key]/recipe[key]
            total_number_batches = round(result)
  return total_number_batches



print(recipe_batches(rec, ingr))
# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))