import os
import openai
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User
from app import db

main = Blueprint('main', __name__)

# --- AUTH ROUTES ---
@main.route("/")
def index():
    return redirect(url_for("main.login"))

@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        hashed_pw = generate_password_hash(password)
        user = User(name=name, email=email, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash("Registered! Please login.")
        return redirect(url_for("main.login"))
    return render_template("register.html")

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("main.home"))
        else:
            flash("Invalid email or password")
    return render_template("login.html")

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))

# --- HOME ---
@main.route("/home")
@login_required
def home():
    return render_template("home.html")

# --- AI STUDY TIP ---
@main.route("/study-tip")
@login_required
def study_tip():
    # Load OpenAI API key from environment
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = "Give a short, practical study tip for a college student staying focused."
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        tip = response.choices[0].text.strip()
    except Exception as e:
        tip = "Sorry, couldn't generate a tip right now."

    return render_template("study_tip.html", tip=tip)

