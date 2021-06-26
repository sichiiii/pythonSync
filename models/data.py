from app import db

class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String())

    def __init__(self, link):
        self.link = link    