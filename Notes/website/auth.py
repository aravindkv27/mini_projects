from flask import Blueprint, render_template, request, flash, redirect, url_for
import re
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def check_email(email):
    if (re.fullmatch(regex,email)):
        return "Valid"
    else:
        return "Invalid"

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in Successfully", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password or email id, try again", category='error')
        else:
            flash("Email does not exist", category='error') 

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('fname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        valid_or_not = check_email(email)
        # print(valid_or_not)

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email Already Exists", category='error')
            print(User.query.all())
        elif valid_or_not == 'Invalid':
            flash("Enter the proper emailid",category="error")
        elif len(first_name) < 2:
            flash("Name should be minimum of 2 letters", category='error')
        elif len(password1) < 8:
            flash("Password required at least 8 characters!",category='error')
        elif len(password1) != len(password2):
            flash("Password Mismatched", category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created Successfully",category='success')
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))


    return render_template("signup.html", user=current_user)