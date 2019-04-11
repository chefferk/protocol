from flask import render_template, request, redirect, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, UserMixin, current_user, login_required
from protocol.models import User, Task2, Task3, Backgrounds, Comments
from protocol import admin, db, create_app
from protocol.utils import Survey
import time
from datetime import datetime

main = Blueprint('main', __name__)

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Task2, db.session))
admin.add_view(ModelView(Task3, db.session))
admin.add_view(ModelView(Backgrounds, db.session))
admin.add_view(ModelView(Comments, db.session))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return True


survey = Survey()


# survey [1]
@main.route('/')
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
@main.route('/organization')
def organization():
    survey.visited_2 = True
    survey.visit_count_2 += 1
    return render_template('organization.html', page_number=2, title='Survey Organization')


# backgroud information [3]
@main.route('/background')
def background():
    survey.visited_3 = True
    survey.visit_count_3 += 1
    # background = Backgrounds(user_id=1, backgrounds='This is my background information in this text field here')
    # db.session.add(background)
    # db.session.commit()
    return render_template('background.html', page_number=3, title='Geological Context of the Study Area')


# Biosignature hypothesis [4]
@main.route('/hypothesis')
def hypothesis():
    survey.visited_4 = True
    survey.visit_count_4 += 1
    return render_template('hypothesis.html', page_number=4, title='Biosignature hypothesis')


# Analyses: PIXL-like XRF (1/2) [5]
@main.route('/analyses1')
def analyses1():
    survey.visited_5 = True
    survey.visit_count_5 += 1
    return render_template('analyses1.html', page_number=5, title='Analyses: PIXL-like XRF')


# Analyses: PIXL-like XRF (2/2) [6]
@main.route('/analyses2')
def analyses2():
    survey.visited_6 = True
    survey.visit_count_6 += 1
    return render_template('analyses2.html', page_number=6, title='Analyses: PIXL-like XRF')


# Task 1/4 [7]
@main.route('/task1')
def task1():
    survey.visited_7 = True
    survey.visit_count_7 += 1
    return render_template('task1.html', page_number=7, title='Task 1/4')


# Outcrop [8]
@main.route('/outcrop')
def outcrop():
    survey.visited_8 = True
    survey.visit_count_8 += 1
    return render_template('outcrop.html', page_number=8, title=False)


# Task 2/4 [9]
@main.route('/task2')
def task2():
    survey.visited_9 = True
    survey.visit_count_9 += 1
    return render_template('task2.html', page_number=9)


# High resolution imagery [10]
@main.route('/highresolution')
def highresolution():
    survey.visited_10 = True
    survey.visit_count_10 += 1
    return render_template('highresolution.html', page_number=10)


# Task 3/4 [11]
@main.route('/task3')
def task3():
    survey.visited_11 = True
    survey.visit_count_11 += 1
    return render_template('task3.html', page_number=11)


# Task 4/4 [12]
@main.route('/task4')
def task4():
    survey.visited_12 = True
    survey.visit_count_12 += 1

    # end timer, save data to db
    if survey.timer_running is True:
        survey.end_timer()

    print(survey)
    return render_template('task4.html', page_number=12)
