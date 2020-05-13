from flask import Flask
from flask import render_template
from NameGenerator import NameGenerator

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return "UP"

@app.route("/name")
def generate():
    name = NameGenerator().name
    print(name)
    return name

if __name__ == "main":
    app.run()
