from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.models import User
from app import db

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return redirect(url_for("main.login"))

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("goals.list_goals"))
        flash("Invalid email or password.")
    return render_template("login.html")

@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = generate_password_hash(request.form.get("password"))
        user = User(email=email, name=name, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("main.login"))
    return render_template("register.html")

@main.route("/home")
@login_required
def home():
    return render_template("home.html")

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))
