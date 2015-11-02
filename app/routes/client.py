from flask import Blueprint, render_template, request, redirect, url_for
from app.forms.organizations import CreateOrganizationForm
from app.models.Organization import Organization
from app.utils import hash_pass
from mongoengine import NotUniqueError

client = Blueprint('client', __name__)

@client.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@client.route('/create_organization', methods=['GET','POST'])
def create_organization():
    form = CreateOrganizationForm(request.form)
    if request.method == 'POST' and form.validate():
        print form.name.data
        print form.email.data
        new_organization = Organization(name=form.name.data, email=form.email.data, password=hash_pass(form.password.data))
        try:
            new_organization.save()
            return redirect(url_for("client.index"))
        except NotUniqueError:
            form.email.errors.append('Duplicate email address.')
    else:
        print "We don't got a new one!"
    return render_template('create_organization.html', form=form)
