from main import db

class Query(db.Model):
    __tablename__ = "queries"

    id = db.Column(db.Integer, primary_key=True)                                      # There is an id column and it is the primary key
    user_id = db.Column(db.Integer, nullable=False, unique=True)                       # user id column, string andit must be unique

    def __repr__(self):                                                               # When printing the model we will see its email attribute
        return f"<Query {self.id}>"