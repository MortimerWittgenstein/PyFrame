import sys, os, time
from flask import Flask, request, render_template, redirect, url_for
from epaper_screen import EPaper

app = Flask(__name__)

@app.route('/')
def home():
        return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'There is no file in form!'

    file = request.files['file']

    eInkScreen = EPaper()
    eInkScreen.displayImage(file)

    return redirect(url_for('home'), code=302)

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'), code=302)

app.run(port=80, host='0.0.0.0')