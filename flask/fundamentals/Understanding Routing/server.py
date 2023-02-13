from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/dojo')
def say_dojo():
    return f"Dojo!"

@app.route('/say/<name>')
def say_hi(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:times>/<name>')
def say_hi_times(name,times):
    return f"{name} <br>" * times

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "Sorry! No response. Try again."

if __name__ =='__main__':
    app.run(debug=True, port=5000)
