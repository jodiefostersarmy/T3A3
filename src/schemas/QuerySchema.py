from main import ma
from models.Query import Query
from marshmallow.validate import Length

class QuerySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Query

    user_id = ma.Integer(required=True, validate=Length(min=1))

query_schema = QuerySchema()
queries_schema = QuerySchema(many=True)