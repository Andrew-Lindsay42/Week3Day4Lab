from app import app
from flask import render_template, request, redirect
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
    if "recurring" in request.form:
        recurring = True
    else:
        recurring = False
    new_event = Event(date, name, guest_number, room_location, description, recurring)
    events.append(new_event)
    return render_template('index.html', events = events)

@app.route('/events/delete/<int:index>', methods = ['POST'])
def delete_event(index):
    events.pop(index)
    return redirect ('/events')

@app.route('/events/edit/<int:index>', methods = ['POST'])
def edit_event(index):
    return render_template('edit.html', index=index, event = events[index])

@app.route('/events/edit/submit/<int:index>', methods = ['POST'])
def edit_event_submit(index):
    date = request.form['date']
    name = request.form['name']
    guest_number = request.form['number']
    room_location = request.form['location']
    description = request.form['description']
    if "recurring" in request.form:
        recurring = True
    else:
        recurring = False
    new_event = Event(date, name, guest_number, room_location, description, recurring)
    events.insert(index, new_event)
    events.pop(index + 1)
    return redirect ('/events')