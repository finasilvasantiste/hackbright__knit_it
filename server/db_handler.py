### Calls to Database are handled here. ###

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    """User in Knit It app."""

    __tablename__ = "users"

    user_email = db.Column(db.String(100), primary_key=True)
    queue_id = db.Column(db.Integer, db.ForeignKey('queues.queue_id'), index=True)

    queue = db.relationship('Queue')


    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<User user_email={self.user_email} queue_id={self.queue_id}>"


class Queue(db.Model):
    """A user's queue."""

    __tablename__ = "queues"

    queue_id = db.Column(db.Integer, primary_key=True)

    # Define relationship to user
    user = db.relationship('User')
    patterns_queue = db.relationship('Patterns_Queue')


    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Queue queue_id={self.queue_id}>"


class Patterns_Queue(db.Model):
    """A user's queue."""

    __tablename__ = "patterns_queues"

    queue_id = db.Column(db.Integer, db.ForeignKey('queues.queue_id'), primary_key=True)
    pattern_id = db.Column(db.Integer, primary_key=True)

    # Define relationship to user
    queue = db.relationship('Queue')


    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Patterns_Queue queue_id={self.queue_id} pattern_id={self.pattern_id}>"



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