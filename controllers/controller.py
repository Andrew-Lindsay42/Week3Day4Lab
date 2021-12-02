from app import app
from flask import render_template, request
from models.events_list import events
from models.event import Event 

@app.route('/events')
def index():
    return render_template('index.html', events = events)