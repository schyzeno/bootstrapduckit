from flask import Flask, render_template
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/grid")
def grid():
    return render_template('grid.html')

@app.route("/grid_typo")
def grid_typo():
    return render_template('grid_typo.html')

@app.route("/table")
def table():
    return render_template('table.html')

@app.route("/form")
def form():
    return render_template('form.html')
