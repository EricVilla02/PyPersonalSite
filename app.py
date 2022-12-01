from flask import Flask
from flask import render_template,request

app = Flask(__name__)

# Function to read in details for page
def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]


@app.route('/')
def homePage():
    name= "Eric Villa"
    details = readDetails('static/details.txt')
    return render_template("base.html", name=name,aboutMe=details)


