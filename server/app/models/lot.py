from ..utils.helper import get_ist_time
from .. import db

class Lot(db.Model):
    __tablename__="lots"
    lot_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    prime_location = db.Column(db.String(200), nullable=False)
    price_per_hour = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(300), nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    no_of_spots = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=get_ist_time())
    
    spots = db.relationship("Spot", back_populates="lot", cascade="all, delete-orphan")

