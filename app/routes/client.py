from flask import Blueprint, render_template

client = Blueprint('client', __name__)

@client.route('/', methods=['GET'])
def index():
    return render_template('index.html')
