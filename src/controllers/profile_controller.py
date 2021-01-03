from models.Profile import Profile
from models.User import User
from schemas.ProfileSchema import profile_schema, profiles_schema
from main import db
from main import bcrypt
from services.auth_service import verify_user 
from sqlalchemy.orm import joinedload
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, abort

profiles = Blueprint("profiles", __name__, url_prefix="/profile")

@profiles.route("/", methods=["GET"])
def profile_index():
    profiles = Profile.query.options(joinedload("user")).all()
    return jsonify(profiles_schema.dump(profiles))

@profiles.route("/", methods=["POST"])
@jwt_required
@verify_user
def profile_create(user):

    if user.profile != []:
        return abort(400, description="User already has profile")

    profile_fields = profile_schema.load(request.json)
    profile = Profile.query.filter_by(username=profile_fields["username"]).first()

    if profile:
        return abort(400, description="username already in use")

    new_profile = Profile()
    new_profile.username = profile_fields["username"]
    new_profile.firstname = profile_fields["firstname"]
    new_profile.lastname = profile_fields["lastname"]
    new_profile.user_id = user.id
    
    user.profile.append(new_profile)
    db.session.commit()
      
    return jsonify(profile_schema.dump(new_profile))

@profiles.route("/<int:id>", methods=["GET"])
def profile_show(id):
    profile = Profile.query.get(id)
    return jsonify(profile_schema.dump(profile))
    

@profiles.route("/<int:id>", methods=["PUT", "PATCH"])
@jwt_required
@verify_user
def profile_update(user, id):                             
    
    profile_fields = profile_schema.load(request.json)
    profile = Profile.query.filter_by(id=id, user_id=user.id)
    if not profile:
        return abort(401, description="Unauthorized to update this profile")

    print(profile.__dict__)
    profile.update(profile_fields)
    db.session.commit()
    return jsonify(profile_schema.dump(profile[0]))


@profiles.route("/<int:id>", methods=["DELETE"])                       # Route for the profile create
@jwt_required        
@verify_user                                                           # Auth service to make sure the correct user owns this profile
def profile_delete(user, id):
    profile = Profile.query.filter_by(id=id, user_id=user.id).first()  # Query the user table with the id and the user id then return the first user
    # print(profile[0].__dict__)
    # return("bills")
    if not profile:                                                    # If there is any number other than 1
        return abort(400, description="Unauthorized to update this profile") # Return this error
    
    db.session.delete(profile)
    db.session.commit()                                                # Commit the session to the db
    return jsonify(profile_schema.dump(profile))                       # Return the deleted profile
