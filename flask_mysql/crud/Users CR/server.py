from flask import Flask, render_template, request, redirect, session
from user_model import User

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def form():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process_form():
    print(f"{request.form} ****************")

    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    #session['id'] = request.form['id']
    #session['created_at'] = request.form['created_at']
    User.create_user(request.form)

    return redirect('/display')

@app.route('/display')
def display():
    users = User.get_all()
    print(f"{request.form} ++++++++++++++++")
    print(f"{session} ------------")
    return render_template("display.html", users = users)


if __name__ == '__main__':
    app.run(debug = True, port=5001)