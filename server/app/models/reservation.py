from .. import db

class Reservation(db.Model):
    __tablename__ = "reservations"
    reservation_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    spot_id = db.Column(db.Integer, db.ForeignKey("spots.spot_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    parking_timestamp = db.Column(db.DateTime, nullable=True)
    leaving_timestamp = db.Column(db.DateTime, nullable=True)
    parking_cost = db.Column(db.Float, nullable=True)
    vehicle_number = db.Column(db.String(20), nullable=False)
    payment_status = db.Column(db.Boolean, nullable=True)  
    
    user = db.relationship("User", back_populates="reservations", uselist=False)
    spot = db.relationship("Spot", back_populates="reservation", uselist=False)