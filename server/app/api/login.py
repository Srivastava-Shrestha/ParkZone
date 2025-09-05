from flask_restful import Resource
from flask import request
from ..models import User,Admin
from ..utils.helper import check_email_format
from flask_jwt_extended import create_access_token

class LoginApi(Resource):
    def post(self):
        data = request.get_json()
        user_or_mail = data.get("user_or_mail")
        password = data.get("password")

        if user_or_mail is None or user_or_mail == "":
            return {'message': "Username or Email Address is required!"}, 401
        if password is None or password == "":
            return {"message": "Password is required!"}, 401
        
        user_or_mail = user_or_mail.lower()
    

        is_email = check_email_format(user_or_mail)

        if is_email:
            admin_by_email = Admin.query.filter_by(email=user_or_mail).first()
            user_by_email = User.query.filter_by(email=user_or_mail).first()
            if admin_by_email:
                if admin_by_email.check_password(password):
                    additional = {'role':'admin', 'id': admin_by_email.admin_id}
                    token = create_access_token(identity=admin_by_email.username, additional_claims=additional)
                    return {"token": token}
                else:
                    return {'message': 'Invalid username or password'}, 401


            if user_by_email:
                if user_by_email.check_password(password):
                    additional = {'role':'user', 'id': user_by_email.user_id}
                    token = create_access_token(identity=user_by_email.username,additional_claims=additional)
                    return {"token": token}
                else:
                    return {'message': 'Invalid username or password'}, 401
                
            else:
                return {'message': 'Account does not exist!'}, 404
            
        else:
            admin_by_username=Admin.query.filter_by(username=user_or_mail).first()
            user_by_username = User.query.filter_by(username=user_or_mail).first()
            if admin_by_username:
                if admin_by_username.check_password(password):
                    additional = {'role':'admin', 'id': admin_by_username.admin_id}
                    token = create_access_token(identity=admin_by_username.username, additional_claims=additional)
                    return {"token": token}
                else:
                    return {'message': 'Invalid username or password'}, 401
                
            if user_by_username:
                if user_by_username.check_password(password):
                    additional = {'role':'user', 'id': user_by_username.user_id}
                    token = create_access_token(identity=user_by_username.username,additional_claims=additional)
                    return {"token": token}
                else:
                    return {'message': 'Invalid username or password'}, 401
                
                
            else:
                return {'message': 'Account does not exist!'}, 404
                

        


