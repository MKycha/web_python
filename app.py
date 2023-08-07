from flask import Flask, render_template, request
from pwd_gen import pwdGenerator
import db 

DB_PATH = "/home/MKycha/web_python/database/site.db"

app = Flask(__name__)

@app.route("/")
def home ():
    return render_template("home.html")

@app.route("/page_2", methods=["GET", "POST"])
def p_2 ():
    result = ""
    if request.method == "POST":
        password = request.form.get("pwd")
        salt = request.form.get("salt")
        n_char = request.form.get("num_char")

        if password != None and salt != None and n_char != None:
            result = pwdGenerator(password, salt, n_char)
        
        db.write_db(DB_PATH, [(password, salt, n_char, result)])

    return render_template("page_2.html", data = result)

@app.route("/page_3")
def p_3 ():
    return render_template("page_3.html", data=db.read_db(DB_PATH))

# Тут обрабатывается GET-запрос с параметрами
@app.route("/test")
def p_4 ():
    # v1 = request.args['var_1']
    v1 = request.args.get("var_1")
    v2 = request.args.get("var_2")
    # return f"Hello from TEST. Var_1 = {v1}, Var_2 = {v2}"
    return render_template('test.html', variable_1 = v1, variable_2 = v2)


def create_app():
    db.create_db(DB_PATH)
    return app