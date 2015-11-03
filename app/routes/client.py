from flask import Blueprint, render_template, session, redirect, url_for, request
from app.forms.organizations import OrganizationLoginForm
from app.models.Organization import Organization
from app.models.Event import Event
from app.models.Member import Member
from app.utils.decorators import redirect_for_no_auth
from app.utils import hash_pass

client = Blueprint('client', __name__)

# Landing Page

@client.route('/', methods=['GET'])
def index():
    return render_template('client/index.html')

# Logged In View

@client.route('/home', methods=['GET'])
@redirect_for_no_auth
def home():
  # Verify these queries; probably redirect if they fail.
  organization = Organization.objects(id=session["organization_id"]).first()
  events = Event.objects(organization=organization)
  number_of_events = events.count()
  members = Member.objects(organization=organization)
  number_of_members = members.count()
  return render_template('client/home.html', **locals())

@client.route('/events', methods=['GET'])
@redirect_for_no_auth
def events():
  organization = Organization.objects(id=session["organization_id"]).first()
  events = Event.objects(organization=organization)
  return render_template('client/events.html', events=events)

@client.route('/members', methods=['GET'])
@redirect_for_no_auth
def members():
  organization = Organization.objects(id=session["organization_id"]).first()
  members = Member.objects(organization=organization)
  return render_template('client/members.html', members=members)

# Authentication

@client.route('/login', methods=['GET','POST'])
def login():
    form = OrganizationLoginForm(request.form)
    if request.method == 'POST' and form.validate():
        users = Organization.objects(email=form.email.data, password=hash_pass(form.password.data))
        if len(users) == 0:
            form.email.errors.append("Invalid login information")
        else:
            session["email"] = users[0].email
            session["organization_id"] = str(users[0].id)
            return redirect(url_for(".home"))
    return render_template('client/login.html', form=form)

@client.route('/logout', methods=['GET','POST'])
def logout():
    session.clear()
    return redirect(url_for("client.index"))