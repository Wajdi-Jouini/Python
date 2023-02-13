from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def form():
    return render_template("index.html")
# ? Action Route  - Form Submit
@app.route('/process', methods=['POST'])
def process_form():
    print(f"{request.form} ****************")

    session['username'] = request.form['username']
    session['location'] = request.form['location']
    session['Language'] = request.form['Language']
    session['comment'] = request.form['comment']

    #! return render_template("display.html")
    return redirect('/result')
# ? Render Page -  Display
@app.route('/result')
def display():
    print(f"{request.form} ++++++++++++++++")
    print(f"{session} ------------")
    return render_template("display.html")

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/result')
    
if __name__ == '__main__':
    app.run(debug = True, port=5001)