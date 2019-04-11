from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import time
from datetime import datetime
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='Admin', template_mode='bootstrap3')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.secret_key = "super secret key"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


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


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Task2, db.session))
admin.add_view(ModelView(Task3, db.session))
admin.add_view(ModelView(Backgrounds, db.session))
admin.add_view(ModelView(Comments, db.session))

# TODO: 1. database to store user input
#       2. determine if we need user sign up/ validation
#       3. figure out how to recored time
#       4. beter javascirpt for selection slides
#       5. build a logging system?
#       6. Currently getting elapsed time for whole survey, do we want time on each page plus total?


class Survey:
    def __init__(self):
        print('Survey object created.')
        self.timer_running = False
        self.visited_1 = False
        self.visited_2 = False
        self.visited_3 = False
        self.visited_4 = False
        self.visited_5 = False
        self.visited_6 = False
        self.visited_7 = False
        self.visited_8 = False
        self.visited_9 = False
        self.visited_10 = False
        self.visited_11 = False
        self.visited_12 = False
        self.visit_count_1 = 0
        self.visit_count_2 = 0
        self.visit_count_3 = 0
        self.visit_count_4 = 0
        self.visit_count_5 = 0
        self.visit_count_6 = 0
        self.visit_count_7 = 0
        self.visit_count_8 = 0
        self.visit_count_9 = 0
        self.visit_count_10 = 0
        self.visit_count_11 = 0
        self.visit_count_12 = 0

    def start_timer(self):
        self.start = time.time()
        self.timer_running = True
        print(f'Timer started at: {self.start}')

    def end_timer(self):
        self.end = time.time()
        self.timer_running = False
        self.elapsed = self.end - self.start
        print(f'Timer ended at: {self.end} \n Elapsed time: {self.elapsed}')

    def __repr__(self):
        return (
            f'Elapsed time: {self.elapsed}\n'
            f'Page 1 visited: {self.visit_count_1} times\n'
            f'Page 2 visited: {self.visit_count_2} times\n'
            f'Page 3 visited: {self.visit_count_3} times\n'
            f'Page 4 visited: {self.visit_count_4} times\n'
            f'Page 5 visited: {self.visit_count_5} times\n'
            f'Page 6 visited: {self.visit_count_6} times\n'
            f'Page 7 visited: {self.visit_count_7} times\n'
            f'Page 8 visited: {self.visit_count_8} times\n'
            f'Page 9 visited: {self.visit_count_9} times\n'
            f'Page 10 visited: {self.visit_count_10} times\n'
            f'Page 11 visited: {self.visit_count_11} times\n'
            f'Page 12 visited: {self.visit_count_12} times\n'
        )


survey = Survey()


# survey [1]
@app.route('/')
def protocol():
    survey.visited_1 = True
    survey.visit_count_1 += 1

    # start timer
    if survey.timer_running is False:
        survey.start_timer()

        # protocol = Protocol(first_name='Keaton',
        #                     last_name='Cheffer',
        #                     email='keaton@tamu.edu')
        # db.session.add(protocol)
        # db.session.commit()

    return render_template('protocol.html', page_number=1, title='Survey Goal')


# survey organization [2]
@app.route('/organization')
def organization():
    survey.visited_2 = True
    survey.visit_count_2 += 1
    return render_template('organization.html', page_number=2, title='Survey Organization')


# backgroud information [3]
@app.route('/background')
def background():
    survey.visited_3 = True
    survey.visit_count_3 += 1
    # background = Backgrounds(user_id=1, backgrounds='This is my background information in this text field here')
    # db.session.add(background)
    # db.session.commit()
    return render_template('background.html', page_number=3, title='Geological Context of the Study Area')


# Biosignature hypothesis [4]
@app.route('/hypothesis')
def hypothesis():
    survey.visited_4 = True
    survey.visit_count_4 += 1
    return render_template('hypothesis.html', page_number=4, title='Biosignature hypothesis')


# Analyses: PIXL-like XRF (1/2) [5]
@app.route('/analyses1')
def analyses1():
    survey.visited_5 = True
    survey.visit_count_5 += 1
    return render_template('analyses1.html', page_number=5, title='Analyses: PIXL-like XRF')


# Analyses: PIXL-like XRF (2/2) [6]
@app.route('/analyses2')
def analyses2():
    survey.visited_6 = True
    survey.visit_count_6 += 1
    return render_template('analyses2.html', page_number=6, title='Analyses: PIXL-like XRF')


# Task 1/4 [7]
@app.route('/task1')
def task1():
    survey.visited_7 = True
    survey.visit_count_7 += 1
    return render_template('task1.html', page_number=7, title='Task 1/4')


# Outcrop [8]
@app.route('/outcrop')
def outcrop():
    survey.visited_8 = True
    survey.visit_count_8 += 1
    return render_template('outcrop.html', page_number=8, title=False)


# Task 2/4 [9]
@app.route('/task2')
def task2():
    survey.visited_9 = True
    survey.visit_count_9 += 1
    return render_template('task2.html', page_number=9)


# High resolution imagery [10]
@app.route('/highresolution')
def highresolution():
    survey.visited_10 = True
    survey.visit_count_10 += 1
    return render_template('highresolution.html', page_number=10)


# Task 3/4 [11]
@app.route('/task3')
def task3():
    survey.visited_11 = True
    survey.visit_count_11 += 1
    return render_template('task3.html', page_number=11)


# Task 4/4 [12]
@app.route('/task4')
def task4():
    survey.visited_12 = True
    survey.visit_count_12 += 1

    # end timer, save data to db
    if survey.timer_running is True:
        survey.end_timer()

    print(survey)
    return render_template('task4.html', page_number=12)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
