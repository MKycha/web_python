from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home ():
    return render_template("home.html")

@app.route("/page_2")
def p_2 ():
    return render_template("page_2.html")

@app.route("/page_3")
def p_3 ():
    return render_template("page_3.html")

def create_app():
    return app