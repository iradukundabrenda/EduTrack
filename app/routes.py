from flask import blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return "Welcome to EduTrack!"

