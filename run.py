from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
import time

app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='Admin', template_mode='bootstrap3')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# ---------- db class ---------- #
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return f'<User {self.username}>'

# TODO: 1. database to store user input
#       2. determine if we need user sign up/ validation
#       3. figure out how to recored time
#       4. beter javascirpt for selection slides
#       5. build a logging system?


# TOC: [1]  Survey goal
#      [2]  Survey organization
#      [3]  Geological context
#      [4]  Biosignature hypothesis
#      [5]  Analyses: PIXL-like XRF (1/2)
#      [6]  Analyses: PIXL-like XRF (2/2)
#      [7]  Task 1/4
#      [8]  Outcrop
#      [9]  Task 2/4
#      [10] Here is a high resolution imagery
#      [11] Task 3/4
#      [12] Task 4/4


# NOTE: this timer seems to be a quick hack with several drawbacks
#       (it would mess up if someone goes back to the first page)
#       a better option might be sessions/cookies
class Survey:
    def __init__(self):
        print('Survey object created.')

    def start_timer(self):
        self.start = time.time()
        print(f'Timer started at: {self.start}')

    def end_timer(self):
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f'Timer ended at: {self.end} \n Elapsed time: {self.elapsed}')


survey = Survey()


# survey [1]
@app.route('/')
def protocol():
    return render_template('protocol.html', page_number=1, title='Survey Goal')


# survey organization [2]
@app.route('/organization')
def organization():
    return render_template('organization.html', page_number=2, title='Survey Organization')


# backgroud information [3]
@app.route('/background')
def background():
    return render_template('background.html', page_number=3, title='Geological Context of the Study Area')


# Biosignature hypothesis [4]
@app.route('/hypothesis')
def hypothesis():
    return render_template('hypothesis.html', page_number=4, title='Biosignature hypothesis')


# Analyses: PIXL-like XRF (1/2) [5]
@app.route('/analyses1')
def analyses1():
    return render_template('analyses1.html', page_number=5, title='Analyses: PIXL-like XRF')


# Analyses: PIXL-like XRF (2/2) [6]
@app.route('/analyses2')
def analyses2():
    return render_template('analyses2.html', page_number=6, title='Analyses: PIXL-like XRF')


# Task 1/4 [7]
@app.route('/task1')
def task1():
    return render_template('task1.html', page_number=7, title='Task 1/4')


# Outcrop [8]
@app.route('/outcrop')
def outcrop():
    return render_template('outcrop.html', page_number=8, title=False)


@app.route('/task2')
def task2():
    return render_template('task2.html', page_number=5)


@app.route('/task3')
def task3():
    return render_template('task3.html', page_number=6)


@app.route('/task4')
def task4():
    return render_template('task4.html', page_number=7)


@app.route('/xrf')
def xrf():
    return render_template('xrf.html', page_number=8)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
