from flask import Blueprint, render_template, request, redirect, url_for, session
from app.forms.organizations import CreateOrganizationForm, OrganizationLoginForm
from app.models.Organization import Organization
from app.utils import hash_pass
from app.utils.decorators import requires_auth
from mongoengine import NotUniqueError
from functools import wraps

organizations = Blueprint('organizations', __name__)

@organizations.route('/', methods=['GET'])
@requires_auth
def index():
    greeting = "Logged In" if "email" in session else "Not Logged In"
    return render_template('index.html', greeting=greeting)

@organizations.route('/create', methods=['GET','POST'])
def create():
    form = CreateOrganizationForm(request.form)
    if request.method == 'POST' and form.validate():
        new_organization = Organization(name=form.name.data, email=form.email.data, password=hash_pass(form.password.data))
        try:
            new_organization.save()
            return redirect(url_for("organizations.index"))
        except NotUniqueError:
            form.email.errors.append('Duplicate email address.')
    return render_template('create_organization.html', form=form)

@organizations.route('/login', methods=['GET','POST'])
def login():
    form = OrganizationLoginForm(request.form)
    if request.method == 'POST' and form.validate():
        users = Organization.objects(email=form.email.data, password=hash_pass(form.password.data))
        if len(users) == 0:
            form.email.errors.append("Invalid login information")
        else:
            session["email"] = users[0].email
            return redirect(url_for("organizations.index"))
    return render_template('organization_login.html', form=form)

@organizations.route('/logout', methods=['GET','POST'])
def logout():
    session.clear()
    return redirect(url_for("index"))

