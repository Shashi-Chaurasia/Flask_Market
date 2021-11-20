# import pymysql
from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rootpass@localhost/user_market'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False , unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False , unique=True)
    description = db.Column(db.String(length=255), nullable=False ,unique=True )

    def __repr__(self):
        return f'Item {self.name}'


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/market')
def market():
    items = Item.query.all()
    return render_template('market.html' , items=items)


if __name__ == '__main__':
    app.run(debug=True)