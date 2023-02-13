from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    all_dojos = Dojo.get_all()
    return render_template('index.html', all_dojos=all_dojos)

@app.route("/dojo", methods=["POST"])
def process_form():
    #print(f"Form from request == {request.form}")
    #session["id"] = request.form["id"]
    #session["dojo_name"] = request.form["dojo_name"]
    id=Dojo.create_dojo(request.form)
    return redirect("/")

@app.route("/create/dojo/<int:id>")

def create_dojo(id):
    this_dojo=Dojo.get_one(id)
    return render_template("index.html", this_dojo=this_dojo)

@app.route('/dojos/<int:dojo_id>/show')
def show_dojo(dojo_id):
    data_dict = {
        'id': dojo_id
    }
    this_dojo = Dojo.get_one(data_dict)
    return render_template('show_dojo.html', this_dojo=this_dojo)