from flask import Flask

def create_app():
    app = Flask(__name__) # start the app from the folder
    app.config['SECRET_KEY'] = 'dev'  # change in production later    



    from app.routes import main
    app.register_blueprint(main)

    return app

