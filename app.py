from flask import Flask, render_template, request, redirect, Blueprint
from flask_cors import CORS

from query import query

app = Flask(__name__)
app.register_blueprint(query)

CORS(app)

@app.route("/")
def home():
    return render_template("./home.html")

@app.route("/querySH")
def qs():
    return render_template("./queryPage.html")

@app.route("/ConQue")
def connor():
    return render_template("./ConQuery.html")