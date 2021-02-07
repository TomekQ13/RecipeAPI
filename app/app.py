from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

recipes = [
    {
    'id': 0,
    'title': 'recipe 1',
    'ingredients': 'apple, flour, juice, water, eggs',
    'instructions': '1. add flour to water. 2. Add sugar. 3. Mix.'},
    {'id': 1,
    'title': 'recipe 2',
    'ingredients': 'pear, beans, juice, water, eggs',
    'instructions': '1. add pear to water. 2. Add eggs. 3. Mix.'},
]

con_string = os.environ.get('MONGO_RECIPEAPP_URI')
cluster = MongoClient(con_string)
db = cluster['RecipeApp']
collection = db['RecipeApp_collection']



@app.route("/recipes")
def recipes_search():
    recipe_id = request.args.get('recipe_id')
    if recipe_id:
        try:
            recipe = recipes[int(recipe_id)]
            return jsonify(recipe)
        except:
            return jsonify({'message': "This recipe doesn't exist."})
    else:
        return jsonify(recipes)

@app.route('/recipe_add', methods = ['POST'])
def add_recipe():
    recipe = request.get_json()
    try:
        if recipe['id'] and recipe['title'] and recipe['ingredients'] and recipe['instructions']:
            recipes.append(recipe)
            return jsonify({'message': 'The recipe has been added'})
    except:
        return jsonify({'message': 'The recipe is missing one of the attributes.'})

@app.route('/recipe_delete', methods=['GET'])
def delete_recipe():
    recipe_id = request.args.get('recipe_id')
    if recipe_id:
        try:
            recipes.pop(int(recipe_id))
            return jsonify({'message': 'The recipe has been deleted.'})
        except:
            return jsonify({'message': 'This recipe does not exist.'})
    else:
        return jsonify({'message': 'Specify a recipe_id as the request parameter.'})

