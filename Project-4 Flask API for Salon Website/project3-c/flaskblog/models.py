from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    account_type = db.Column(db.String(120), unique=False, nullable=False)
    
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}',  '{self.image_file}')"


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patron_account = db.Column(db.String(100), nullable=False)
    stylist_account = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    hour = db.Column(db.String(100), nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Appointment('{self.day}', '{self.hour},{self.patron_account}', '{self.stylist_account}')"
