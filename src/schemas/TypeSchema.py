from main import ma
from models.Type import Type
from marshmallow.validate import Length, OneOf

class TypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Type

    type_name = ma.String(validate=OneOf(["image", "video", "album"]))

type_schema = TypeSchema()
types_schema = TypeSchema(many=True)