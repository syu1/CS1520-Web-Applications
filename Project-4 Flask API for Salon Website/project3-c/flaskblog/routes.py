import os
import secrets

from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app, db
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm,AppointmentForm
from flaskblog.models import User, Appointment
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        password =  User.query.filter_by(password=form.password.data).first()

        if form.username.data == 'owner' and form.password.data =='pass':
            flash('Welcome owner!')
            login_user(user, remember=form.remember.data)
            return redirect(url_for('owner'))

        
        elif user and password and user.account_type == 'stylist' :
            login_user(user, remember=form.remember.data)   
            return redirect(url_for('style_profile', my_username=user.username))

        elif user and password and user.account_type == 'patron' :
            login_user(user, remember=form.remember.data)   
            return redirect(url_for('patron_profile'))

        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
    

@app.route("/owner")
def owner():
    stylists = []
    users = User.query.all()
    for user in users:
        if(user.account_type == "stylist"):
            stylists.append(user)
    return render_template('owner.html', stylists=stylists)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
   
    form = RegistrationForm()
    if form.validate_on_submit():
        
        user = User(username=form.username.data,account_type="patron", password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))





@app.route("/style_profile/<string:my_username>", methods=['GET', 'POST'])
@login_required
def style_profile(my_username):
    appointments = []
    appointments = Appointment.query.all()
    for appointment in appointments:
        if(appointment.stylist_account == my_username):
            appointments.append(appointment)
    return render_template('style_profile.html',username = my_username, appointments=appointments)

@app.route("/patron_profile", methods=['GET', 'POST'])
@login_required
def patron_profile():
    stylists = []
    users = User.query.all()
    for user in users:
        if(user.account_type == "stylist"):
            stylists.append(user)
    return render_template('patron_profile.html',stylists=stylists)







@app.route("/new_stylist", methods=['GET', 'POST'])
def new_stylist():
    
    form = RegistrationForm()
    if form.validate_on_submit():
        
        user = User(username=form.username.data,account_type="stylist", password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('New Stylist Created!', 'success')
        return redirect(url_for('owner'))
    return render_template('new_stylist.html', title='stylist', form=form)

@app.route("/new_appointment", methods=['GET', 'POST'])
def new_appointment():
    
    form = AppointmentForm()
    if form.validate_on_submit():
        
        appointment = Appointment(patron_account=form.patron_username.data, stylist_account=form.stylist_username.data, date=form.date.data, hour = form.hour.data)
        db.session.add(appointment)
        db.session.commit()
        flash('Appointment Created', 'success')
        return redirect(url_for('patron_profile'))
    return render_template('new_appointment.html', title='appointments', form=form)





