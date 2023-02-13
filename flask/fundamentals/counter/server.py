from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def Num_Visits():
    if "num" not in session:
        session["num"]=0
    else:
        session["num"] +=1
    return render_template("index.html")

@app.route('/two')
def two_Visits():
    if "num" not in session:
        session["num"]=0
    else:
        session["num"] +=2
    return render_template("index.html")

@app.route('/<int:num>')
def Add_Visits(num):
    return render_template("index.html",num=num)

@app.route('/destroy_session')
def clear_session():
    session.clear()
    return redirect('/')

    
if __name__ == '__main__':
    app.run(debug = True, port=5001)