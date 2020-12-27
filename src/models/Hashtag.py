from main import db

class Hashtag(db.Model):
    __tablename__ = "hashtags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self):                                                               # When printing the model we will see its email attribute
        return f"<User {self.id}>"