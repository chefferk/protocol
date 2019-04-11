from datetime import datetime
from flask import current_app
from protocol import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ---------- db class ---------- #
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=True)
    last_name = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    create_date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    admin = db.Column(db.Boolean, nullable=True, default=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    elapsed_time = db.Column(db.Float(10), unique=False, nullable=True)
    backgrounds = db.relationship('Backgrounds', backref='user')
    task2 = db.relationship('Task2', backref='user')
    comments = db.relationship('Comments', backref='user')

    def __repr__(self):
        return f'<User {self.first_name}, {self.elapsed_time}>'


class Task2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task2_rationale1 = db.Column(db.Text, nullable=True)
    task2_rationale2 = db.Column(db.Text, nullable=True)
    task2_a_pos = db.Column(db.String(100), nullable=True)
    task2_b_pos = db.Column(db.String(100), nullable=True)
    task2_c_pos = db.Column(db.String(100), nullable=True)
    task2_d_pos = db.Column(db.String(100), nullable=True)
    task2_e_pos = db.Column(db.String(100), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Task2 {self.task2_rationale1}, {self.task2_rationale2}>'


class Task3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task3_rationale1 = db.Column(db.Text, nullable=True)
    task3_rationale2 = db.Column(db.Text, nullable=True)
    task3_a_pos = db.Column(db.String(100), nullable=True)
    task3_b_pos = db.Column(db.String(100), nullable=True)
    task3_c_pos = db.Column(db.String(100), nullable=True)
    task3_d_pos = db.Column(db.String(100), nullable=True)
    task3_e_pos = db.Column(db.String(100), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Task2 {self.task3_rationale1}, {self.task3_rationale2}>'


class Backgrounds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    backgrounds = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Task2 {self.user_id}, {self.backgrounds}>'


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comments = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Task2 {self.user_id}, {self.comments}>'
