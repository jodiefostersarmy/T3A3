from main import db

class Type(db.Model):
    __tablename__ = "types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)

    def __repr__(self):
        return f"<User {self.id}>"