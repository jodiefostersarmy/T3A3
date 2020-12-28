from main import ma                                                     # Import the serialization object from main
from models.Hashtag import Hashtag
from marshmallow.validate import Length    

class HashtagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Hashtag
    
    phrase = ma.String(required=True, validate=Length(min=1))

hashtag_schema = HashtagSchema()
hashtags_schema = HashtagSchema(many=True)