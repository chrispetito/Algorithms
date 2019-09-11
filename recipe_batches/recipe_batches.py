#!/usr/bin/python

import math

rec = { 'milk': 100, 'butter': 50, 'cheese': 10 }
ingr = { 'milk': 198, 'butter': 52, 'cheese': 10 }

def recipe_batches(recipe, ingredients):
  # determine whether or not all ingredients are present
  print(len(recipe))
  recipe_array = []
  ingredients_array = []
  for x in recipe:
    recipe_array.append(recipe[x])
  for y in ingredients:
    ingredients_array.append(ingredients[y])
  for i in range(0, len(recipe_array)):
    print(recipe_array[i])

x = dict(a=1, b=2)
y = dict(a=2, b=2)

shared_items = {value: rec[value] for value in rec if value in ingr and rec[value] == ingr[value]}
print(f'shared: {(shared_items)}')


print(recipe_batches(rec, ingr))
# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))