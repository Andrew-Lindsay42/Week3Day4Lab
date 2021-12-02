from app import app
from flask import render_template, request
from models.events_list import events
from models.event import Event 

@app.route('/events')
def index():
    return render_template('index.html', events = events)

@app.route('/events', methods = ['POST'])
def add_event():
    date = request.form['date']
    name = request.form['name']
    guest_number = request.form['number']
    room_location = request.form['location']
    description = request.form['description']
    new_event = Event(date, name, guest_number, room_location, description)
    events.append(new_event)
    return render_template('index.html', events = events)