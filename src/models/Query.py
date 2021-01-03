from main import db

class Query(db.Model):
    __tablename__ = "queries"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, unique=True)

    def __repr__(self):
        return f"<Query {self.id}>"