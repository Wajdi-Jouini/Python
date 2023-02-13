from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user import User

@app.route('/')
def form():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process_form():
    print(f"{request.form} ****************")

    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['id'] = request.form['id']
    session['updated_at'] = request.form['updated_at']
    session['created_at'] = request.form['created_at']

    #IMPORTANT
    x = User.create_user(request.form)
    print(x,"*"*50)
    return redirect(f'/display/{x}')


@app.route('/display')
def display():
    users = User.get_all()
    print(f"{request.form} ++++++++++++++++")
    print(f"{session} ------------")
    return render_template("display.html", users = users)

@app.route('/display')
def display_new(user_id):
    users = User.delete_user(data_dict)
    print(f"{request.form} ++++++++++++++++")
    print(f"{session} ------------")
    return render_template("display.html", users = users)

@app.route("/display/<int:user_id>")
def show_user(user_id):
    data_dict = {'id': user_id}
    user = User.get_one(data_dict)
    return render_template("one_user.html" , user = user)

@app.route("/display/<int:user_id>/edit")
def edit_user(user_id):
    data_dict = {'id': user_id}
    user = User.get_one(data_dict)
    return render_template("edit.html" , user = user)

@app.route('/display/<int:user_id>/delete')
def delete(user_id):
    User.delete({'id':user_id})
    return redirect(f'/display')

@app.route('/display/update', methods=['POST'])
def update():
    user_id = request.form['id']
    User.update(request.form)
    return redirect(f'/display/<int:user_id>')