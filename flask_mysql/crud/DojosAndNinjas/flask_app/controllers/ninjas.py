from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route("/ninjas", methods=["POST"])
def ninjas_form():
    print(f"Form from request == {request.form}")
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["age"] = request.form["age"]
    data={
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.create_ninja(data)
    return redirect("/")

@app.route('/ninjas')
def add_ninja():
    all_dojos = Dojo.get_all()
    return render_template('new_ninja.html', all_dojos=all_dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect("/")