import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route("/work")
def work():
    return render_template('work.html')

@app.route("/hobbies")
def hobbies():
    return render_template('hobbies.html')

@app.route("/travel")
def travel():
    return render_template('travel.html')

