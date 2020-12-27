from main import ma                                                    # Import the serialization object from main
from models.Type import Type                                           # Importign the Type model
# from marshmallow.validate import Length                                # Import the length class that will allow us to validate the length of the string 

class TypeSchema(ma.SQLAlchemyAutoSchema):                             # Generates Schema automatically
    class Meta:
        model = Type                                                   # Generate Schema using the Type Model

    # email = ma.String(required=True, validate=Length(min=4))         # The email is required and must be at least 6 chars long
    # password = ma.String(required=True, validate=Length(min=6))      # The email is required and must be at least 6 chars long


type_schema = TypeSchema()                                             # Schema for a single type
types_schema = TypeSchema(many=True)                                   # Schema for multiple types    