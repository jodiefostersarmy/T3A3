from main import db
from datetime import datetime
from sqlalchemy.orm import backref

class Media(db.Model):
    __tablename__ = "medias"
    
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(), nullable=False)
    media_url = db.Column(db.String(), nullable=False)
    permalink = db.Column(db.String(), nullable=True, unique=True)
    thumbnail_url = db.Column(db.String(), nullable=False, unique=True)
    timestamp = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"<Media {self.id}>"