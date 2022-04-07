from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, ProductionConfig, Config
import pymysql

pymysql.install_as_MySQLdb()
db = SQLAlchemy()


def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    with app.app_context():
        from api import routes
        app.register_blueprint(routes.bp)
        db.create_all()

    return app
