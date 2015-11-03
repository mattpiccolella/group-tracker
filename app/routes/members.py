from flask import Blueprint, render_template, redirect, url_for, request, session
from app.models.Event import Event
from app.models.Member import Member
from app.models.Organization import Organization
from app.utils import is_authenticated

members = Blueprint('members', __name__)

@members.route('/<member_id>', methods=['GET'])
def detail(member_id):
  try:
    member = Member.objects(id=member_id).first()
    if member != None:
      events = Event.objects(attendees__in=[member])
      return render_template("members/detail.html", member=member, events=events, auth=is_authenticated())
  except:
    pass
  return render_template("error/404.html"), 404
