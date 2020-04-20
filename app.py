"""from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
	return "Hello World"

@app.route("/david")
def david():
	return "Hello David"

@app.route("/<string:name>")
def hello(name):
	name = name.capitalize()
	return "<h1>Hello {}</h1>".format(name)
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
