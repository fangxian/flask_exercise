from flask1 import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    add_time = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return 'user table'
