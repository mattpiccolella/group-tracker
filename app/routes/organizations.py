from flask import Blueprint, render_template, request, redirect, url_for, session
from app.forms.organizations import CreateOrganizationForm, OrganizationLoginForm
from app.models.Organization import Organization
from app.routes.client import client
from app.utils import hash_pass
from mongoengine import NotUniqueError
from functools import wraps

organizations = Blueprint('organizations', __name__)

@organizations.route('/<organization_id>', methods=['GET'])
def detail(organization_id):
    try:
        organization = Organization.objects(id=organization_id).first()
        if organization != None:
            return render_template("organizations/detail.html", organization=organization)
    except:
        pass
    return render_template("error/404.html"), 404

@organizations.route('/create', methods=['GET','POST'])
def create():
    form = CreateOrganizationForm(request.form)
    if request.method == 'POST' and form.validate():
        new_organization = Organization(name=form.name.data, email=form.email.data, password=hash_pass(form.password.data))
        try:
            new_organization.save()
            session["email"] = new_organization.email
            session["organization_id"] = str(new_organization.id)
            return redirect(url_for("client.home"))
        except NotUniqueError:
            form.email.errors.append('Duplicate email address.')
    return render_template('organizations/create.html', form=form)