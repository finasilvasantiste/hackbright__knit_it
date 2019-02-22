### Data Model for db data is defined here. ###

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Users(db.Model):
    """Movie on ratings website."""

    __tablename__ = "users"

    user_email = db.Column(db.String(100), primary_key=True)
    queue_id = db.Column(db.Integer)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<User user_email={self.user_email} queue_id={self.queue_id}>"





