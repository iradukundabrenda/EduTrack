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

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Try logging in.', 'error')
            return redirect(url_for('main.register'))

        hashed_password = generate_password_hash(password)
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('main.register'))

    return render_template('register.html')

