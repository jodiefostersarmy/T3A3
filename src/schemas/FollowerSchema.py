from main import ma
from models.Follow import Follow
from marshmallow.validate import Length

class FollowSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Follow
    
    follower_id = ma.Nested("UserSchema", only=("id"))
    following_id = ma.Nested("UserSchema", only=("id"))

follow_schema = FollowSchema()
follows_schema = FollowSchema(many=True)