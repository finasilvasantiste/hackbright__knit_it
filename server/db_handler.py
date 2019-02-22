### Calls to Database are handled here. ###

from flask_sqlalchemy import SQLAlchemy
from model_db import Users

db = SQLAlchemy()


class DB_Handler():


    def connect_to_db(self, app):
        """Connect the database to our Flask app."""

        # Configure to use our PostgreSQL database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5434/hackbright'
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ratings'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_ECHO'] = True
        db.app = app
        db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app


    DB_HANDLER = DB_Handler()

    DB_HANDLER.connect_to_db(app)
    print("Connected to DB.")