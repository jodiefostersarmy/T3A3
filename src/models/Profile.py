from main import db

class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    lastname = db.Column(db.String(), nullable=False)
    biography = db.Column(db.String(), nullable=False)
    profilepic = db.Column(db.String(), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    

    def __repr__(self):
        return f"<Profile {self.username}>"