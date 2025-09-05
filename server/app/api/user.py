from flask_restful import Resource
from flask import request

from ..models import User
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..utils.helper import role_required

class UserApi(Resource):
    @jwt_required()
    @role_required("admin")
    def get(self, user_id=None):
        try:
            if user_id is None:
                all_users = User.query.all()
                user_details = [{
                    "user_id": user.user_id,
                    "username": user.username,
                    "email": user.email,
                    "address": user.address,
                    "pincode": user.pincode
                    
                } for user in all_users]
                return user_details, 200
            else:
                user = User.query.filter_by(user_id=user_id).first()
                if user:
                    user_detail = {
                    "user_id": user.user_id,
                    "username": user.username,
                    "email": user.email,
                    "address": user.address,
                    }
                    return user_detail, 200
                else:
                    return {"message": "User not found"}, 400
                
        except Exception as e:
            return {"message": f"Something went wrong!"}, 500
