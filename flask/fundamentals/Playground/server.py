from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def Welcome():
    return render_template("index.html", times=3, color="blue")

@app.route('/play/<int:times>')
def welcome1(times):
    return render_template("index.html", times= times, color="blue")

@app.route('/play/<int:times>/<color>')
def welcome2(times,color):
    return render_template("index.html", times= times, color=color)


if __name__ =='__main__':
    app.run(debug=True, port=5000)
