from datetime import datetime
from flask import current_app
from protocol import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# -------------------- user db -------------------- #
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=True)
    last_name = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    create_date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    admin = db.Column(db.Boolean, nullable=True, default=False)
    complete = db.Column(db.Boolean, nullable=False, default=False)
    elapsed_time = db.relationship('Elapsed_times', backref='user')
    backgrounds = db.relationship('Backgrounds', backref='user')
    task2 = db.relationship('Task2', backref='user')
    comments = db.relationship('Comments', backref='user')

    def __repr__(self):
        return f'<User {self.first_name}, {self.email}, {self.complete}>'


# -------------------- task 2 db -------------------- #
class Task2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rational = db.Column(db.Text, nullable=True)
    position = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Task2 {self.position}, {self.rational}>'


# -------------------- task 3 db -------------------- #
class Task3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rationals = db.Column(db.Text, nullable=True)
    positions = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Task3 {self.positions}, {self.rationals}>'


# -------------------- backgrounds db -------------------- #
class Backgrounds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    backgrounds = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Backgrounds {self.user_id}, {self.backgrounds}>'


# -------------------- comments db -------------------- #
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comments = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Comments {self.user_id}, {self.comments}>'


# -------------------- elapsed times db -------------------- #
class Elapsed_times(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    elapsed_times = db.Column(db.Float(10), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def get_time(self):
        return float(self.elapsed_times)

    def __repr__(self):
        return f'<Elapsed_times {self.elapsed_times}>'
