from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello From server.py"

@app.route('/hello/<name>')
def say_hi(name):
    return f"Hello {name} 😁😘"

@app.route('/hello/<name>/<int:times>/<color>')
def say_hi_times(name,times,color):
    # return f"Hello {name} 😁😘"*int(times)
    #return f"Hello {name} 😁😘"* times
    return render_template("index.html", user=name, times= times, color=color)


if __name__ =='__main__':
    app.run(debug=True, port=5001)