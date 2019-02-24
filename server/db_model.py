### Data Model for db data is defined here. ###

from flask_sqlalchemy import SQLAlchemy
import hashlib
from random import randint

db = SQLAlchemy()

class User(db.Model):
    """
        Represents a user in Knit It app.
    """

    __tablename__ = "users"

    user_email = db.Column(db.String(100), primary_key=True)
    queue_id = db.Column(db.Integer, unique=True, index=True)
    password_hash = db.Column(db.String(500), nullable=False)

    queue = db.relationship('Queue')

    def __init__(self, user_email, queue_id, password):
        self.user_email = user_email
        self.queue_id = queue_id
        self.password_hash = User.get_password_hash(password)


    @classmethod
    def get_password_hash(self,password):

        sha = hashlib.sha1(password.encode('utf-8'))
        
        return str(sha.hexdigest())


    @classmethod
    def get_patterns_from_user(self, user):
        """
            Returns list of patterns in user's queue.
        """
        patterns = user.queue

        return patterns


    @classmethod
    def get_all_queue_ids(self):
        """
            Returns list with all queue_ids in db.
        """
        
        all_users = User.query.all()

        queue_ids = []

        for user in all_users:
            queue_ids.append(user.queue_id)

        return queue_ids


    @classmethod
    def get_new_queue_id(self):
        """
            Returns a new queue_id that is not yet in use.
        """
        queue_ids = self.get_all_queue_ids()

        new_queue_id = randint(1, 10000)

        while new_queue_id in queue_ids:

            new_queue_id = randint(1, 10000)

        return new_queue_id




    def __repr__(self):
        """
            Provides helpful representation when object is printed.
        """

        return "<User user_email={} queue_id={} password_hash={}>".format(self.user_email,
            self.queue_id, self.password_hash)



class Queue(db.Model):
    """
        Represents a user's queue.
    """

    __tablename__ = "queues"

    queue_id = db.Column(db.Integer, db.ForeignKey('users.queue_id'), primary_key=True)
    pattern_id = db.Column(db.Integer, primary_key=True)

    # Define relationship to user
    user = db.relationship('User')


    def __init__(self, queue_id, pattern_id):
        self.queue_id = queue_id
        self.pattern_id = pattern_id


    @classmethod
    def get_users_from_pattern(self, pattern):
        """
            Returns list of users who have the same pattern in queue.
        """
        pattern_id = pattern.pattern_id

        queues_with_pattern = Queue.query.filter(Queue.pattern_id==pattern_id).all()

        users = []

        for q in queues_with_pattern:
            users.append(q.user)


        return users


    def __repr__(self):
        """
            Provides helpful representation when object is printed.
        """

        return "<Queue queue_id={} pattern_id={}>".format(self.queue_id, self.pattern_id)



class DB_Connection_Handler():


    def connect_to_db(self, app):
        """
            Connect the database to Flask app.
        """

        # Configure to use our PostgreSQL database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5434/hackbright'
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ratings'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_ECHO'] = True
        db.app = app
        db.init_app(app)

    def add_new_object(self, object_to_add):
        
        db.session.add(object_to_add)
        db.session.commit()


def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from server import app


    DB__CONNECTION_HANDLER = DB_Connection_Handler()

    DB__CONNECTION_HANDLER.connect_to_db(app)
    print("Connected to DB.")


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    init_app()
    