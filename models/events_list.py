from models.event import Event
import datetime

event_1 = Event(datetime.date(2021, 12, 2), "Codeclan Lab", 2, "Main Space", "Flask templates lab", False)
event_2 = Event(datetime.date(2021, 12, 2), "Social", 16, "Pub", "Everyone goes for a drink", True)

events = [event_1, event_2]