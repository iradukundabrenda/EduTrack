from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import Goal

goal_bp = Blueprint("goals", __name__)

@goal_bp.route("/", methods=["GET"])
@login_required
def list_goals():
    goals = Goal.query.filter_by(user_id=current_user.id).all()
    return render_template("goals.html", goals=goals)

@goal_bp.route("/add", methods=["POST"])
@login_required
def add_goal():
    title = request.form.get("title")
    description = request.form.get("description")
    if title:
        g = Goal(title=title, description=description, user_id=current_user.id)
        db.session.add(g)
        db.session.commit()
    return redirect(url_for("goals.list_goals"))

@goal_bp.route("/update/<int:goal_id>", methods=["POST"])
@login_required
def update_goal(goal_id):
    g = Goal.query.get_or_404(goal_id)
    g.progress = int(request.form.get("progress", g.progress))
    db.session.commit()
    return redirect(url_for("goals.list_goals"))

@goal_bp.route("/delete/<int:goal_id>", methods=["POST"])
@login_required
def delete_goal(goal_id):
    g = Goal.query.get_or_404(goal_id)
    db.session.delete(g)
    db.session.commit()
    return redirect(url_for("goals.list_goals"))

@goal_bp.route("/data")
@login_required
def goals_data():
    goals = Goal.query.filter_by(user_id=current_user.id).all()
    return jsonify([{"title": g.title, "progress": g.progress} for g in goals])

