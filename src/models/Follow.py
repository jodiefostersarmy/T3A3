from main import db

class Follow(db.Model):
    __tablename__ = "followers"

    id = db.Column(db.Integer, primary_key=True)
    followee_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"<Profile {self.username}>"