from main import ma
from models.Media import Media
from marshmallow.validate import Length

class MediaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Media

    caption = ma.String()
    media_url = ma.String(required=True, validate=Length(min=5))
    permalink = ma.String()
    thumbnail_url = ma.String(required=True)
    timestamp = ma.DateTime(required=True)

media_schema = MediaSchema()
medias_schema = MediaSchema(many=True)