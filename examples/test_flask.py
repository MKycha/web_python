from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, Flask!</h1>"

@app.route("/second")
def page_2():
    return "<h1>Hello, from PAGE 2!</h1>"

if __name__ == "__main__":
    app.run()