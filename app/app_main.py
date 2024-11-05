from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from sqlite3 import Error
import os
from main import FictionalChocoHouse

def create_app():
    application = Flask(__name__)
    application.secret_key = "d4d68adfc046579d752916505b72d581"
    return application

app = create_app()
db = FictionalChocoHouse()

@app.route('/')
def home():
    flavours = db.get_all_flavours()
    ingredients = db.get_all_ingredients()
    suggestions = db.get_all_suggestions()
    return render_template('index.html', flavours=flavours, ingredients=ingredients, suggestions=suggestions)

@app.route('/new_flavour', methods=['POST'])
def new_flavour():
    name = request.form['name']
    description = request.form['description']
    is_seasonal = 1 if request.form.get('is_seasonal', 'off') == 'on' else 0
    season = request.form['season'] if is_seasonal else None
    db.add_flavour(name, description, is_seasonal, season)
    flash('Flavour added successfully!')
    return redirect(url_for('home'))

@app.route('/new_ingredient', methods=['POST'])
def new_ingredient():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    unit = request.form['unit']
    allergen_info = request.form.get('allergen_info')
    db.add_ingredient(name, quantity, unit, allergen_info)
    flash("Ingredient added successfully")
    return redirect(url_for('home'))

@app.route('/new_suggestion', methods=['POST'])
def new_suggestion():
    flavour_name = request.form['flavour_name']
    description = request.form['description']
    allergen_concerns = request.form.get('allergen_concerns')
    db.add_suggestion(flavour_name, description, allergen_concerns)
    flash('Suggestion added successfully!')
    return redirect(url_for('home'))

@app.route('/edit_suggestion/<int:suggestion_id>', methods=['POST'])
def edit_suggestion(suggestion_id):
    new_status = request.form['status']
    db.update_suggestion_status(suggestion_id, new_status)
    flash('Suggestion status updated!')
    return redirect(url_for('home'))

if __name__ == "__main__":
    db = FictionalChocoHouse()
    print("Starting the Flask application!")
    app.run(debug=True)