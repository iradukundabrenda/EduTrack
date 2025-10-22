from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

    db.init_app(app)

    from app.routes import main  # make sure this path is correct
    from app.routes.goal_routes import goal_bp

    app.register_blueprint(main)
    app.register_blueprint(goal_bp)

    login_manager = LoginManager()
    login_manager.login_view = 'main.login'  # <-- This must match Blueprint name + function
    login_manager.login_message_category = 'info'
    login_manager.init_app(app)

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

