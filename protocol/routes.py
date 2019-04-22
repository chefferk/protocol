from flask import render_template, request, redirect, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, UserMixin, current_user, login_required, logout_user, login_user
from protocol.models import User, Task2, Task3, Backgrounds, Comments, Elapsed_times
from protocol import admin, db, create_app
from protocol.utils import Survey
from protocol.forms import RegistrationForm, BackgroundForm, CommentsForm
import time
from datetime import datetime
import json
import pprint
import logging
import ast

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)


main = Blueprint('main', __name__)

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Task2, db.session))
admin.add_view(ModelView(Task3, db.session))
admin.add_view(ModelView(Backgrounds, db.session))
admin.add_view(ModelView(Comments, db.session))
admin.add_view(ModelView(Elapsed_times, db.session))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return True


survey = Survey()


# ------------------- login ------------------- #
@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.protocol'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            login_user(user)
            return redirect(url_for('main.protocol'))
        else:
            user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('main.protocol'))

    return render_template('login.html', title='Login', form=form)


# ------------------- survey [1] ------------------- #
@main.route('/')
@login_required
def protocol():
    if current_user.complete:
        return redirect(url_for('main.landingpage'))
    survey.visited_1 = True
    survey.visit_count_1 += 1

    # TODO: need to prevent people from taking multiple time... check for elapsed time/ completed db
    #       send to new page

    # start timer
    if survey.timer_running is False:
        survey.start_timer()

    return render_template('protocol.html', page_number=1, title='Survey Goal')


# ------------------- survey organization [2] ------------------- #
@main.route('/organization')
@login_required
def organization():
    if current_user.complete:
        return redirect(url_for('main.landingpage'))
    survey.visited_2 = True
    survey.visit_count_2 += 1
    return render_template('organization.html', page_number=2, title='Survey Organization')


# ------------------- backgroud information [3] ------------------- #
@main.route('/background')
@login_required
def background():
    if current_user.complete:
        return redirect(url_for('main.landingpage'))
    survey.visited_3 = True
    survey.visit_count_3 += 1
    return render_template('background.html', page_number=3, title='Geological Context of the Study Area')


# ------------------- Biosignature hypothesis [4] ------------------- #
@main.route('/hypothesis')
@login_required
def hypothesis():
    if current_user.complete:
        return redirect(url_for('main.landingpage'))
    survey.visited_4 = True
    survey.visit_count_4 += 1
    return render_template('hypothesis.html', page_number=4, title='Biosignature hypothesis')


# ------------------- Analyses: PIXL-like XRF (1/2) [5] ------------------- #
@main.route('/analyses1')
@login_required
def analyses1():
    if current_user.complete:
        return redirect(url_for('main.landingpage'))
    survey.visited_5 = True
    survey.visit_count_5 += 1
    return render_template('analyses1.html', page_number=5, title='Analyses: PIXL-like XRF')


# ------------------- Analyses: PIXL-like XRF (2/2) [6] ------------------- #
@main.route('/analyses2')
@login_required
def analyses2():
    if current_user.complete:
        return redirect(url_for('main.landingpage'))
    survey.visited_6 = True
    survey.visit_count_6 += 1
    return render_template('analyses2.html', page_number=6, title='Analyses: PIXL-like XRF')


# ------------------- Task 1/4 [7] ------------------- #
@main.route('/task1', methods=['GET', 'POST'])
@login_required
def task1():
    if current_user.complete:
        return redirect(url_for('main.landingpage'))
    survey.visited_7 = True
    survey.visit_count_7 += 1

    # TODO: need to write a check to see if alrady submitted background...
    #       let them edit in future.

    user = Backgrounds.query.filter_by(user_id=current_user.id).first()
    if not user:
        form = BackgroundForm()
        if form.validate_on_submit():
            background = Backgrounds(backgrounds=form.background.data, user_id=current_user.id)
            db.session.add(background)
            db.session.commit()
            return redirect(url_for('main.outcrop'))
    else:
        form = False

    return render_template('task1.html', page_number=7, title='Task 1/4', form=form)


# ------------------- Outcrop [8] ------------------- #
@main.route('/outcrop')
@login_required
def outcrop():
    if current_user.complete:
        return redirect(url_for('main.landingpage'))
    survey.visited_8 = True
    survey.visit_count_8 += 1
    return render_template('outcrop.html', page_number=8, title=False)


# ------------------- Task 2/4 [9] ------------------- #
@main.route('/task2')
@login_required
def task2():
    if current_user.complete:
        return redirect(url_for('main.landingpage'))
    survey.visited_9 = True
    survey.visit_count_9 += 1

    loc = {}
    task2 = Task2.query.filter_by(user_id=current_user.id).first()
    if task2:
        location = Task2.query.filter_by(user_id=current_user.id).first()
        location = ast.literal_eval(location.position)
        location.pop('length', None)

        bad_key = None
        for key, value in location.items():
            temp = json.loads(location[key])
            if temp['className'] == 'Transformer':
                bad_key = key
        
        location.pop(bad_key, None)
        rational = task2.rational

        loc = {}
        for key, value in location.items():
            temp = json.loads(location[key])
            x = temp['attrs']['x']
            y = temp['attrs']['y']
            try:
                rotation = temp['attrs']['rotation']
            except Exception as e:
                rotation = 0
            value = temp['attrs']['value']
            loc[key] = {'x': x, 'y': y, 'value': value, 'rotation': rotation}
    else:
        location = ''
        rational = ''

    if request.method == 'GET' and request.args:
        form = request.args
        position = form['location']
        print(position)
        rational = form['rational']
        parsed = json.loads(position)
        if not task2:
            task2 = Task2(position=str(parsed), rational=rational, user_id=current_user.id)
            db.session.add(task2)
            db.session.commit()
        else:
            task2 = Task2.query.filter_by(user_id=current_user.id).first()
            task2.position = str(parsed)
            task2.rational = rational
            db.session.commit()
        if form['action'] == 'back':
            return redirect(url_for('main.outcrop'))
        else:
            return redirect(url_for('main.highresolution'))

    return render_template('task2.html', page_number=9, threshold=45, visited=survey.visited_9, locations=loc, rational=rational)


# ------------------- High resolution imagery [10] ------------------- #
@main.route('/highresolution')
@login_required
def highresolution():
    if current_user.complete:
        return redirect(url_for('main.landingpage'))
    survey.visited_10 = True
    survey.visit_count_10 += 1
    return render_template('highresolution.html', page_number=10)


# ------------------- Task 3/4 [11] ------------------- #
@main.route('/task3')
@login_required
def task3():
    if current_user.complete:
        return redirect(url_for('main.landingpage'))
    survey.visited_11 = True
    survey.visit_count_11 += 1

    loc = {}
    task3 = Task3.query.filter_by(user_id=current_user.id).first()
    if task3:
        locations = Task3.query.filter_by(user_id=current_user.id).first()
        locations = ast.literal_eval(locations.positions)
        locations.pop('length', None)

        bad_key = None
        for key, value in locations.items():
            temp = json.loads(locations[key])
            if temp['className'] == 'Transformer':
                bad_key = key
        
        locations.pop(bad_key, None)

        loc = {}
        for key, value in locations.items():
            temp = json.loads(locations[key])
            x = temp['attrs']['x']
            y = temp['attrs']['y']
            try:
                rotation = temp['attrs']['rotation']
            except Exception as e:
                rotation = 0
            value = temp['attrs']['value']
            loc[key] = {'x': x, 'y': y, 'value': value, 'rotation': rotation}
    else:
        locations = ''

    if request.method == 'GET' and request.args:
        form = request.args
        positions = form['locations']
        parsed = json.loads(positions)
        if not task3:
            task3 = Task3(positions=str(parsed), user_id=current_user.id)
            db.session.add(task3)
            db.session.commit()
        else:
            task3 = Task3.query.filter_by(user_id=current_user.id).first()
            task3.positions = str(parsed)
            db.session.commit()
        if form['action'] == 'back':
            return redirect(url_for('main.highresolution'))
        else:
            return redirect(url_for('main.task4'))

    return render_template('task3.html', page_number=11, threshold=960, visited=survey.visited_11, locations=loc)


# ------------------- Task 4/4 [12] ------------------- #
@main.route('/task4', methods=['GET', 'POST'])
@login_required
def task4():
    if current_user.complete:
        return redirect(url_for('main.landingpage'))
    survey.visited_12 = True
    survey.visit_count_12 += 1

    form = CommentsForm()
    if form.validate_on_submit():
        # end timer, save data to db
        if survey.timer_running is True:
            survey.end_timer()
            timer = Elapsed_times(elapsed_times=survey.elapsed, user_id=current_user.id)
            user = User.query.filter_by(id=current_user.id).first()
            user.complete = True
            db.session.add(timer)
        comments = Comments(comments=form.comments.data, user_id=current_user.id)
        db.session.add(comments)
        db.session.commit()
        return redirect(url_for('main.landingpage'))

    # print(survey)
    return render_template('task4.html', page_number=12, form=form)


# ------------------- landing page ------------------- #
@main.route("/landingpage")
@login_required
def landingpage():
    logout_user()
    return render_template('landingpage.html')


# ------------------- logout ------------------- #
@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))


@main.route('/test')
def test():
    return render_template('test.html', threshold=960)


@main.route('/test2')
def test2():
    footprints = {
        1: {
            'x': 160,
            'y': 450,
            'value': 132
        },
        2: {
            'x': 360,
            'y': 160,
            'value': 74
        }
    }
    return render_template('test2.html', threshold=960, footprints=footprints)


@main.route('/test3')
def test3():
    return render_template('test3.html', threshold=960)
