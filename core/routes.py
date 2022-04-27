from core import app, db
from flask import render_template, redirect, url_for, flash
from core.models import Items, Users, Role
from core.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/summary')
@login_required
def summary():
    items = db.session.query(Items).all()
    return render_template('summary.html', items = items)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = Users(first_name = form.first_name.data, last_name = form.last_name.data, email = form.email.data, password = form.password.data, role=form.role.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash(f'Account created succesfully, you are now logged in as {new_user.first_name} ', category='success')
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for err in form.errors.values():
            flash(f'Operation failed: {err}', category = 'danger')
    return render_template('register.html', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Users.query.filter_by(email = form.email.data).first()

        if attempted_user and attempted_user.check_password(attempted_password = form.password.data):
            login_user(attempted_user)
            flash(f'Login succesful', category='success')
            return redirect(url_for('home_page'))
        else:
            flash(f'username or passoword incorrect', category='danger')



    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    logout_user()
    flash(f'you have been logged out', category='info')
    return redirect(url_for('home_page'))