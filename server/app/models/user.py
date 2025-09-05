from collections import UserList
from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    
    reservations = db.relationship("Reservation", back_populates="user", cascade="all, delete-orphan")
    notifications = db.relationship("Notification", back_populates="user", cascade="all, delete-orphan" )
    
    def hash_password(self,password):
        hashed_password = generate_password_hash(password)
        self.password = hashed_password

    def check_password(self,password):
        return check_password_hash(self.password,password)