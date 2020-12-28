from main import db

class Hashtag(db.Model):
    __tablename__ = "hashtags"

    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        return f"< {self.phrase} >"