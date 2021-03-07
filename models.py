from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    date_joined = db.Column(db.DateTime)

##The below is just a test. Usually these go into app.py inside the functions of the routes

def insertData():
    from datetime import datetime

    newUser = User(name="Foo", date_joined=datetime.now())
    db.session.add(newUser)
    db.session.commit()
