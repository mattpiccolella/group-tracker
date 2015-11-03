from flask import Blueprint, render_template, redirect, url_for, request, session
from app.forms.events import CreateEventForm, EventCheckinForm
from app.models.Event import Event
from app.models.Member import Member
from app.models.Organization import Organization
from app.routes.client import client
from app.utils.decorators import requires_auth
from app.utils import is_authenticated

events = Blueprint('events', __name__)

@events.route('/<event_id>', methods=['GET'])
def detail(event_id):
  try:
    event = Event.objects(id=event_id).first()
    if event != None:
      return render_template("events/detail.html", event=event, auth=is_authenticated())
  except:
    pass
  return render_template("error/404.html"), 404

@events.route('/<event_id>/check_in', methods=['GET','POST'])
def check_in(event_id):
  form = EventCheckinForm(request.form)
  message = ""
  if request.method == 'POST' and form.validate():
    try:
      # TODO: Fix this. It's a little bit janky.
      event = Event.objects(id=event_id).first()
      if event != None:
        member = Member.objects(name=form.name.data, organization=event.organization).first()
        if member == None:
          member = Member(name=form.name.data, organization=event.organization)
          member.save()
        event = Event.objects(id=event_id, attendees__nin=[member]).first()
        if event != None:
          event.attendees.append(member)
          event.save()
          message = "Successfully checked in."
        else:
          message = "You have already checked in to this event."
    except:
      return render_template("error/404.html"), 404
  return render_template("events/check_in.html", form=form, message=message)


@events.route('/create', methods=['GET','POST'])
@requires_auth
def create():
  form = CreateEventForm(request.form)
  if request.method == 'POST' and form.validate():
    organization = Organization.objects(id=session["organization_id"]).first()
    new_event = Event(name=form.name.data, organization=organization)
    new_event.save()
    return redirect(url_for('client.events'))
  return render_template('events/create.html', form=form)

