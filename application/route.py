from application import app
from flask import render_template

import pyaudio
import wave

#Handles http://127.0.0.1:5000/
@app.route('/') 
@app.route('/index') 
@app.route('/home') 
def index_page(): 
    return render_template("index.html")

@app.route('/record')
def record_audio():
    
    return render_template("index.html")
