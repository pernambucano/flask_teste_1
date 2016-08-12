from app import db

class BlogPost(db.Model):
    """docstring for BlogPost."""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<{} - {}>'.format(self.title, self.description)
