from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, User
from werkzeug.security import generate_password_hash


main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to EduTrack!"

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Hash the password before storing
        hashed_password = generate_password_hash(password, method='sha256')

        # Save user to the database
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('main.register'))

    return render_template('register.html')
