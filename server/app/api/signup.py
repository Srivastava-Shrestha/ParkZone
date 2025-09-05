from flask_restful import Resource
from flask import request
from ..models import User
from .. import db
from ..utils.helper import check_email_format, check_username_format

class SignupApi(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        address = data.get("address")
        pincode = data.get("pincode")

        if email is None or email == "":
            return {'message':'Email Address is required!'}, 400
        if username is None or username == "":
            return {'username is required!'}, 400
        if password is None or password == "":
            return {'message':'Password is required!'}, 400
        if confirm_password is None or confirm_password == "":
            return {'message':'Confirm password is required!'}, 400
        if address is None or address == "":
            return {'message':'Address is required!'}, 400
        if pincode is None or pincode == "":
            return {'message':'Pincode is required!'}, 400
        
        email = email.lower()
        username = username.lower()

        if not check_email_format(email):
            return {'message':'Email Address is invalid!'}, 400
        if not check_username_format(username):
            return {'message':'Username is invalid!'}, 400

        if bool(User.query.filter_by(username=username).first()):
            return {'message':'This Username is already in use!'}, 400      
        if bool(User.query.filter_by(email=email).first()):
            return {'message':'This Email address is already in use!'}, 400

        if password and confirm_password:
            if len(password) < 8 or len(confirm_password) < 8:
                return {'message': 'Password must be at least 8 characters!'}, 400
            if password != confirm_password:
                return {'message': 'Password and Confirm Password must be same!'}, 400

        try:
            new_user = User(username=username, email=email, address=address, pincode=pincode)
            new_user.hash_password(password)
            db.session.add(new_user)
            db.session.commit()
            return {'message':'Signed up successfully!'}, 200
        
        except Exception as e:
            db.session.rollback()
            return {'message':f'An error occurred str{e}'}, 500

