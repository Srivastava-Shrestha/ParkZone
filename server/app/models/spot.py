from .. import db

class Spot(db.Model):
    __tablename__ = "spots"
    spot_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    lot_id = db.Column(db.Integer, db.ForeignKey("lots.lot_id"), nullable=False)
    status = db.Column(db.Boolean, default=True)

    lot = db.relationship("Lot", back_populates="spots", uselist=False)
    reservation = db.relationship("Reservation", back_populates="spot", cascade="all, delete-orphan")
