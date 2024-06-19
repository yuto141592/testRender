import os
from flask import Flask
from .extensions import db
from .routes import main
from config import Config

def create_app():
    app = Flask(__name__)

    #app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    #postgres://imagepicapp_user:ZeXYZxkVbbxX7TcmiyyPLMs6EC9HL2NL@dpg-cpo5coo8fa8c73bbo7hg-a.singapore-postgres.render.com/imagepicapp
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(main)

    return app

app = create_app()

if __name__ == "__main__":
    app.run()
