from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template('upload.html')
