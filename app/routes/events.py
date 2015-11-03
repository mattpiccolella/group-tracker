from flask import Blueprint, render_template, redirect, url_for, request
from app.forms.events import CreateEventForm
from app.models.Event import Event

events = Blueprint('events', __name__)

@events.route('/', methods=['GET'])
def index():
    return redirect(url_for(".detail", event_id=5000))

@events.route('/<event_id>', methods=['GET'])
def detail(event_id):
  response = render_template("error/404.html"), 404
  try:
    event = Event.objects(id=event_id).first()
    if event:
      response = render_template("events/detail.html", event=event)
  except:
    pass
  return response

@events.route('/create', methods=['GET','POST'])
def create():
  form = CreateEventForm(request.form)
  if request.method == 'POST' and form.validate():
    new_event = Event(name=form.name.data)
    new_event.save()
    return redirect(url_for('.detail',event_id=new_event.id))
  return render_template('events/create.html', form=form)

