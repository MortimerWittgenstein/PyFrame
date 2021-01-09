import sys, os, time
import RPi.GPIO as GPIO
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

#app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'pictures')

@app.route('/')
def home():
        return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'there is no file in form!'
    file = request.files['file']
    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)

    from epaper_screen import EPaper

    eInkScreen = EPaper()
    eInkScreen.displayImage(path)

    os.remove(path)

    return redirect(url_for('home'), code=302)

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'), code=302)

app.run(port=80, host='0.0.0.0')