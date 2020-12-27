from main import db

class Type(db.Model):
    __tablename__ = "types"

    id = db.Column(db.Integer, primary_key=True)                                      # There is an id column and it is the primary key
    name = db.Column(db.String(), nullable=False, unique=True)                        # Name column, string andit must be unique

    def __repr__(self):                                                               # When printing the model we will see its email attribute
        return f"<User {self.id}>"