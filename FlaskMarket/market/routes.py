from market import app
from flask import render_template
from market.models import Item
from market.forms import Registration

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/market')
def market():
    items = Item.query.all()
    return render_template('market.html' , items=items)


@app.route('/resiter')
def user_resiter():
    forms = Registration()
    return render_template('register.html' , forms=forms)